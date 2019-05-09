#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 08 12:44:49 2019

@author: Vaibhav Maurya
"""

class DataPreprocessing:
    
    def __init__(self, d):
        import json as js
        from string import Template as t
        import shutil
        import os
        import pandas as pd
        import sqlite3 as sql
        import traceback
        import numpy as np
        import re
        from dateutil.parser import parse
        
        self.re = re
        self.js = js
        self.t = t
        self.shell_utill = shutil
        self.os_mod = os
        self.src_dir = d['raw']
        self.clean_data_dir = d['clean']
        self.process_dir = d['process']
        self.datastructure_json = d['parser']
        self.db_dir = d['db']
        self.pd = pd
        self.db = sql
        self.traceback = traceback
        self.np = np 
        self.parse = parse 
        self.data_parser = self.readDataParser()
        self.data_parser["aColIndices"] = []
        for k,v in self.data_parser["data_cols"].items():
            self.data_parser["aColIndices"].append(v["pos"])
        
    def readDataParser(self):
        with open(self.datastructure_json) as f:
            data_parser = self.js.load(f)
            return data_parser
        
    def getTemplate(self, seperator=","):
        p = seperator+"$"
        return self.t("$"+p.join(self.data_parser['data_cols'].keys()))
    
    def parseString(self, a):
        p = self.data_parser['data_cols']
        return {k:a[v['start'] - 1:v['size']+v['start'] - 1].strip() for k,v in p.items()}
    
    def parseTemplateForString(self, a, seperator=","):
        g = self.getTemplate(seperator)
        return g.substitute(self.parseString(a))

    def dateparser(self,x):
        try:
            return self.parse(x).strftime("%Y-%m-%d %H:%M:%S")
        except:
            return '2000-01-01 00:00:00'
        
    def read_process_cleandata(self, filename, buffersize):
        csv_reader = None
        path = self.os_mod.path.join(self.clean_data_dir,filename)
        if not self.os_mod.path.exists(path):
            print("NOT FOUND clean data file: {}".format(path))
            return None
        print("Found clean data file: {}".format(path))
        csv_reader = self.pd.read_csv(path, parse_dates={'ETD_DATETIME':['ETD_DATE','ETD_TD_TIME']}, chunksize=buffersize, date_parser=self.dateparser)
        print("csv chunk reader created {}".format(csv_reader))
        return csv_reader

    def connect_db(self, db_name):
        if not self.os_mod.path.exists(self.db_dir):
            print("Db directory is not correct")
            return False
        conn = self.db.connect(self.os_mod.path.join(self.db_dir,db_name))
        print('connection established : {}'.format(conn))
        return conn

    
    def get_table_rowcount(self, conn, tablename):
        p = conn.execute("select count(*) from {}".format(tablename))
        g = p.fetchall()
        print(" Count has been selected from table {}".format(tablename))
        print(" Count has been selected from table is here {}".format(g))        
        return g


    def clean_db_table(self, conn, tablename):
        conn.execute("delete from {}".format(tablename))
        conn.commit()
        print("Table has been truncated number of rows are {}".format(self.get_table_rowcount(conn, tablename)))
        

    def is_table_exists(self, conn, tablename):
        print(" TABLE EXISTS ?? ")
        s = "SELECT name FROM sqlite_master WHERE type='table' AND name='{}'".format(tablename)
        print(" firing query {}".format(s))
        p = conn.execute(s)
        return len(p.fetchall()) == 1
    
    def write_to_db(self, db_name, tablename, csv_reader):
        count_chnk = 1
        conn = self.connect_db(db_name)
        print(" Here got the DB: {}".format(conn))
        print(" Here got the Table: {}".format(tablename))
        print(" Here got the db name: {}".format(db_name))
        if not conn and not tablename and not csv_reader:
            print("write_to_db >> one or more object is missing")
            return False
        
        try:
            print(" First cleaning table: {}".format(tablename))
            if self.is_table_exists(conn, tablename):
                print(" TABLE EXISTS !!! ")
                # self.clean_db_table(conn, tablename)
                print("{} table has rows : {}".format(tablename, self.get_table_rowcount(conn, tablename)))
                
            for chunk in csv_reader:
                chunk.to_sql(tablename, con=conn, if_exists='append', index_label='ID')
                print(" writing chunk : {}".format(count_chnk))
                count_chnk+=1
            conn.commit()
        
            print("Table {} has been fetched with data".format(tablename))
            print("{} table has rows : {}".format(tablename,self.get_table_rowcount(conn, tablename)))
        except Exception as ex:
            print("   ****  EXCEPTION ***  ")
            print(''.join(self.traceback.format_exception(etype=type(ex), value=ex, tb=ex.__traceback__)))
            conn.close()
        else:
            conn.close()
        
        
    def parseTxtAndPrn(self, p):
           return self.parseTemplateForString(p)

    def parseCSV(self, p):
        return ",".join(self.np.array(p.split(','))[self.data_parser["aColIndices"]])

    def isCSV(self, data_file):
        return data_file.lower().endswith(".csv")

    def isTxtOrLstFile(self, data_file):
        return data_file.lower().endswith(".txt") or data_file.lower().endswith(".lst")

    def isExcelFile(self, data_file):
        return data_file.lower().endswith(".xlsx") or data_file.lower().endswith(".xls")
        
    def clean_data(self, data_file, clean_data_file):       
        read_flag = False
        fMethod = None
        b_CsvFlag = False
        if not self.os_mod.path.exists(data_file):
            print(">>> Data File does not exist")
            return

        if self.isCSV(data_file):
            fMethod = self.parseCSV
            b_CsvFlag = True
            print("CSV file it is ")
        elif self.isTxtOrLstFile(data_file):
            fMethod = self.parseTxtAndPrn
            print("Text or lst file it is ")
        else:
            print(">>>>>This file is not recognized<<<<<< \n\n")
            return

        if self.os_mod.path.exists(clean_data_file):
            fw = open(clean_data_file,'a+')
            print(">>> File already exists here")
        else:
            fw = open(clean_data_file,'w+')
            print(">>> Created New output File")
            fw.write(",".join(self.data_parser['data_cols'].keys()))
            fw.write("\n")
        
        with open(data_file) as f:
            p = f.readline()
            while p:
                if 'ETD_WAYBILL_NO' in p:
                    p = f.readline()
                    p = f.readline()
                    read_flag = True
                    continue
                if read_flag:
                    if b_CsvFlag and len(p.split(',')) < 45:
                        read_flag = False
                    elif len(p) < 120:
                        read_flag = False
                    else:
                        g = fMethod(p)
                        fw.write(g)
                        fw.write("\n")
                p = f.readline()               
        fw.close()
        
    def processData(self, format='csv', isOneFile=True):
        self.reset_all()
        ext = "."+format
        if isOneFile:
            q = self.os_mod.path.join(self.clean_data_dir,'full_data'+'.'+format)
        print(">>>>> Data cleaning starts <<<<<<<")    
        for file in self.os_mod.listdir(self.src_dir):
            afile_ext = self.re.findall(r'\.txt|\.csv|\.lst',file.lower())
            if len(afile_ext) > 0:
                p = self.os_mod.path.join(self.src_dir,file)
                if not isOneFile:
                    q = self.os_mod.path.join(self.clean_data_dir,file)
                    q = q.replace(afile_ext[0],ext)
                print("new format is {}".format(q))
                self.clean_data(p,q)
                self.shell_utill.move(p,self.process_dir)
                
    
    def write_processeddata_db(self, db_name, tablename, filename='full_data.csv', buffersize=100000):
        reader = self.read_process_cleandata(filename, buffersize)
        self.write_to_db(db_name, tablename, reader)
        
    def reset_all(self):
        for file in self.os_mod.listdir(self.process_dir):
            print("file {} is moving to raw directory".format(file))
            self.shell_utill.move(self.os_mod.path.join(self.process_dir,file),self.src_dir)
        
        for file in self.os_mod.listdir(self.clean_data_dir):
            print("file {} is getting deleted from clean_data directory".format(file))
            self.os_mod.remove(self.os_mod.path.join(self.clean_data_dir,file))
        print(">>>>> Data files are reset <<<<<<<")
        
        
        
        
            
        
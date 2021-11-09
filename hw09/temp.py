#!/usr/bin/env python3
# Based pm: https://github.com/googleworkspace/python-samples/tree/master/sheets/quickstart
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START sheets_quickstart]
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import time, sys
import glob

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1WFt2pcTjp-55zFXNzGb9ekktZibOxfmuAbW247G6iuA'
SAMPLE_RANGE_NAME = 'A2'

base_dir = '/sys/bus/w1/devices/'
device_folder3 = glob.glob(base_dir + '28-00000cf9d76a')[0]
device_file3 = device_folder3 + '/w1_slave'

device_folder2 = glob.glob(base_dir + '28-00000cf9c527')[0]
device_file2 = device_folder2 + '/w1_slave'

device_folder1 = glob.glob(base_dir + '28-00000cfa4fc9')[0]
device_file1 = device_folder1 + '/w1_slave'

BUS="i2c-1"
ADDR="0x40"
siPATH="/sys/class/i2c-adapter/" + BUS + "/1-0040/iio:device1/"
tmpPATH="/sys/class/hwmon/hwmon0/"
sleepTime=5

def read_temp_raw(device_file):
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp(device_folder, device_file):
    lines = read_temp_raw(device_file)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw(device_file)
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_f

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            # creds = flow.run_local_server(port=0)
            creds = flow.run_console()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    
    firstTime = True
    while True:
        # Get current temp and humidity
        # Temp seems a bit low, add an offset
        # output Nan if frst time to graphs will be disconnected.
        if firstTime:
            firstTime = False
            values = [ [time.time()/60/60/24+ 25569 - 5/24, read_temp(device_folder1, device_file1), read_temp(device_folder2, device_file2), read_temp(device_folder3, device_file3)]]
            body = {'values': values}
            result = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                        range=SAMPLE_RANGE_NAME,
                                        valueInputOption='USER_ENTERED', 
                                        body=body
                                        ).execute()
        #offset = 2.8
        #fd = open(siPATH + "in_temp_raw")
        #temp = str(float(fd.read().replace('\n', ''))/100 + offset)
        #fd.close()
        
        #fd = open(siPATH + "in_humidityrelative_raw")
        #humid = str(float(fd.read().replace('\n', ''))/100)
        #fd.close()
    
        #fd = open(tmpPATH + "temp1_input")
        #temp2 = float(fd.read().replace('\n', ''))/1000
        #temp2 = 9/5*temp2 + 32
        #fd.close()
    
        values = [ [time.time()/60/60/24+ 25569 - 5/24, read_temp(device_folder1, device_file1), read_temp(device_folder2, device_file2), read_temp(device_folder3, device_file3)]]
        body = {'values': values}
        result = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME,
                                    valueInputOption='USER_ENTERED', 
                                    body=body
                                    ).execute()
        # print(result)
        time.sleep(sleepTime)

if __name__ == '__main__':
    main()
# [END sheets_quickstart]

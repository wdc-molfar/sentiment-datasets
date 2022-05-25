#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys
import fasttext

if __name__ == "__main__":
    lang = sys.argv[1] #format of input languale is "uk", "ru" or "en"
    
    model = fasttext.load_model(os.path.join('models', lang+'.ftz'))
    # DISPLAY ACCURACY OF TRAINED MODEL
    validation = model.test(os.getcwd()+'/test/'+lang+'.txt')      
    text_line = "accuracy: " + str(validation[1]) +'\n' 
    print(text_line)
    
    validation_label = model.test_label(os.getcwd()+'/test/'+lang+'.txt')
    print ('__label__pos', validation_label['__label__pos'])
    print ('__label__neg', validation_label['__label__neg'])

# -*- coding: utf-8 -*-
# -*- mode: python -*-

"""packages to import"""
from __future__ import print_function, division, absolute_import
import os
import h5py

"""Functions for file IO"""

def data_unpack(data):
    """
    This function unpacks the given .gz file. The argument is the file name (ex: s1.tar.gz).
    """
    tar -zxvf data
    
def load_data(subject):
    """
    This function loads the data collected from a given subject (s1-s7) 
    from the data set fcx-3 from crcns.org, and then saves the data under the variable
    named "data." The argument is the subject name (ex: "s1").
    """
    path = os.path.join("data", subject, "data_primary.mat")
    data= h5py.File(path, mode='r')
    return data
def data_attributes(subject):
    """
    This function loads the data collected froma given subject, using the function load_data
    as described above. The module then returns the file within the data set, and the shape
    and data type of this file. The file "data_primary.mat" that is downloaded for each
    subject contains only one file, so the list of the data keys only returns one object.
    """
    data = load_data(subject)
    file = list(data.keys())
    dset = data[file[0]]
    shape = dset.shape
    data_type = dset.dtype
    return file,dset,shape,data_type

def select_data(subject)
    """
    This function loads the data, same as before. Then, with the square brackets we can select a 
    choice of rows or columns that we would like to see in particular in the data. We select rows 
    using slicing, from the first row we want to see to the last([:]), with the last being non-inclusive,
    returing a list of wanted rows. For selecting columns, we create a list of specific columns we want to 
    focus on. We can compare/contrast two different columns that we want to focus on in the data.  
    """
    data= load.data(subject) 
    row=data[1:2]
    column=data["//whatever column we want to select"]
    multiple_columns=data[["//","//"]]

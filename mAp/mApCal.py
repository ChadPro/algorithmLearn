# -- coding: utf-8 --
# Copyright 2018 The LongYan. All Rights Reserved.
from __future__ import absolute_import
from __future__ import division
import numpy as np

####################
#   complex func   #
#   use boxes iou  #
####################
l_cal_type = ["accuracy", "recall", "precision"]
def sample_detect_cal(positive, lables, boxes, detections, detections_boxes, cal_type="recall"):
    """
    Arguments:
      positive: positive class index, int
      labels: sample label list
      boxes: sample obj boxes
      detections: sample detection list
      detections_boxes: sample detection boxes list
      cal_type: sample cal type
    Return:
      sample detection statistics caculate
    """
    TP = 0
    FN = 0
    FP = 0
    TN = 0

    for i, one_labels in enumerate(lables):
        pass
    pass

####################
#   simple func    #
####################
def cal_precision(positive, label, detection):
    """
    Arguments:
      positive: positive class index, int
      label: sample label list
      detection: sample detection list
    Return:
      sample detection accuracy TP/(TP+FP)
    """
    TP = 0
    FN = 0
    FP = 0
    TN = 0
    for i, one_label in enumerate(label):
        if one_label == positive:
            if detection[i] == one_label:
                TP += 1
            else:
                FN += 1
        else:
            if detection[i] == positive:
                FP += 1
            else:
                TN += 1
    
    if TP+FP == 0:
        return 0
    else:
        return float(TP/(TP+FP))

def cal_recall(positive, label, detection):
    """
    Arguments:
      positive: positive class index, int
      label: sample label list
      detection: sample detection list
    Return:
      sample detection accuracy TP/(TP+FN)
    """
    TP = 0
    FN = 0
    FP = 0
    TN = 0
    for i, one_label in enumerate(label):
        if one_label == positive:
            if detection[i] == one_label:
                TP += 1
            else:
                FN += 1
        else:
            if detection[i] == positive:
                FP += 1
            else:
                TN += 1
    
    if TP+FN == 0:
        return 0
    else:
        return float(TP/(TP+FN))

def cal_acc(positive, label, detection):
    """
    Arguments:
      positive: positive class index, int
      label: sample label list
      detection: sample detection list
    Return:
      sample detection accuracy TP/len(label)
    """
    TP = 0
    FN = 0
    FP = 0
    TN = 0
    for i, one_label in enumerate(label):
        if one_label == positive:
            if detection[i] == one_label:
                TP += 1
            else:
                FN += 1
        else:
            if detection[i] == positive:
                FP += 1
            else:
                TN += 1
    

    return float((TP+TN)/len(label))
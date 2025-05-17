# -*- coding: utf-8 -*-
import os
import ExtractFeatures
import xml.etree.ElementTree as ET

import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction import DictVectorizer
from sklearn import svm

path = 'nnc_updated_ah\\cs\\a07.xml'

X, y, X_test, y_test, test_sen, train_sen = [], [], [], [], [], []
temp = 0


trainFeatures = [{'prev-word': '', 'next-word': 'निर्वाचन', 'word': 'आम'}, {'prev-word': 'आम', 'next-word': 'मा', 'word': 'निर्वाचन'}, {'prev-word': 'निर्वाचन', 'next-word': 'स्पष्ट', 'word': 'मा'}, {'prev-word': 'मा', 'next-word': 'बहुमत', 'word': 'स्पष्ट'}, {'prev-word': 'स्पष्ट', 'next-word': 'ल्याए', 'word': 'बहुमत'}, {'prev-word': 'बहुमत', 'next-word': 'को', 'word': 'ल्याए'}, {'prev-word': 'ल्याए', 'next-word': 'नेपाली', 'word': 'को'}, {'prev-word': 'को', 'next-word': 'काँग्रेस', 'word': 'नेपाली'}, {'prev-word': 'नेपाली', 'next-word': 'को', 'word': 'काँग्रेस'}, {'prev-word': 'काँग्रेस', 'next-word': 'संसदीय', 'word': 'को'}, {'prev-word': 'को', 'next-word': 'दल', 'word': 'संसदीय'}, {'prev-word': 'संसदीय', 'next-word': 'का', 'word': 'दल'}, {'prev-word': 'दल', 'next-word': 'नेता', 'word': 'का'}, {'prev-word': 'का', 'next-word': 'को', 'word': 'नेता'}, {'prev-word': 'नेता', 'next-word': 'रुप', 'word': 'को'}, {'prev-word': 'को', 'next-word': 'मा', 'word': 'रुप'}, {'prev-word': 'रुप', 'next-word': 'श्री', 'word': 'मा'}, {'prev-word': 'मा', 'next-word': 'गिरीजा', 'word': 'श्री'}, {'prev-word': 'श्री', 'next-word': 'प्रसाद', 'word': 'गिरीजा'}, {'prev-word': 'गिरीजा', 'next-word': 'कोइराला', 'word': 'प्रसाद'}, {'prev-word': 'प्रसाद', 'next-word': 'ले', 'word': 'कोइराला'}, {'prev-word': 'कोइराला', 'next-word': 'पन्द्रह', 'word': 'ले'}, {'prev-word': 'ले', 'next-word': 'सदस्यीय', 'word': 'पन्द्रह'}, {'prev-word': 'पन्द्रह', 'next-word': 'मन्त्रि', 'word': 'सदस्यीय'}, {'prev-word': 'सदस्यीय', 'next-word': 'परिषद', 'word': 'मन्त्रि'}, {'prev-word': 'मन्त्रि', 'next-word': 'को', 'word': 'परिषद'}, {'prev-word': 'परिषद', 'next-word': 'गठन', 'word': 'को'}, {'prev-word': 'को', 'next-word': 'गरी', 'word': 'गठन'}, {'prev-word': 'गठन', 'next-word': 'सक्नु', 'word': 'गरी'}, {'prev-word': 'गरी', 'next-word': 'भए', 'word': 'सक्नु'}, {'prev-word': 'सक्नु', 'next-word': 'पछि', 'word': 'भए'}, {'prev-word': 'भए', 'next-word': 'मुलुक', 'word': 'पछि'}, {'prev-word': 'पछि', 'next-word': 'को', 'word': 'मुलुक'}, {'prev-word': 'मुलुक', 'next-word': 'ध्यान', 'word': 'को'}, {'prev-word': 'को', 'next-word': 'राष्ट्रिय', 'word': 'ध्यान'}, {'prev-word': 'ध्यान', 'next-word': 'सभा', 'word': 'राष्ट्रिय'}, {'prev-word': 'राष्ट्रिय', 'next-word': 'को', 'word': 'सभा'}, {'prev-word': 'सभा', 'next-word': 'गठन', 'word': 'को'}, {'prev-word': 'को', 'next-word': 'र', 'word': 'गठन'}, {'prev-word': 'गठन', 'next-word': 'त्यस', 'word': 'र'}, {'prev-word': 'र', 'next-word': 'पछि', 'word': 'त्यस'}, {'prev-word': 'त्यस', 'next-word': 'हुने', 'word': 'पछि'}, {'prev-word': 'पछि', 'next-word': 'संसद', 'word': 'हुने'}, {'prev-word': 'हुने', 'next-word': 'को', 'word': 'संसद'}, {'prev-word': 'संसद', 'next-word': 'अधिवेशन', 'word': 'को'}, {'prev-word': 'को', 'next-word': 'तिर', 'word': 'अधिवेशन'}, {'prev-word': 'अधिवेशन', 'next-word': 'केन्द्रित', 'word': 'तिर'}, {'prev-word': 'तिर', 'next-word': 'हुन', 'word': 'केन्द्रित'}, {'prev-word': 'केन्द्रित', 'next-word': 'थाले', 'word': 'हुन'}, {'prev-word': 'हुन', 'next-word': 'को', 'word': 'थाले'}, {'prev-word': 'थाले', 'next-word': 'छ', 'word': 'को'}, {'prev-word': 'को', 'next-word': '।', 'word': 'छ'}, {'prev-word': 'छ', 'next-word': '', 'word': '।'}]
trainLabels = ['JX', 'NN', 'II', 'JX', 'NN', 'VE', 'IKM', 'NN', 'NN', 'IKM', 'JX', 'NN', 'IKO', 'NN', 'IKM', 'NN', 'II', 'NN', 'NP', 'NP', 'NP', 'IE', 'MM', 'JX', 'NN', 'NN', 'IKM', 'NN', 'VR', 'VI', 'VE', 'II', 'NN', 'IKM', 'NN', 'JX', 'NN', 'IKM', 'NN', 'CC', 'DDX', 'II', 'VN', 'NN', 'IKM', 'NN', 'II', 'JX', 'VI', 'VE', 'IKM', 'VVYN1', 'YF']
test_feat =[]
test = ['संसद', 'को', 'अधिवेशन', 'आषाढ', 'को', 'शुरु', 'मा', 'हुने', 'राष्ट्रियसभा', 'को', 'गठन', 'यै', 'महिना', 'मा', 'भईसक्ने', 'चीन-सोभियत', 'सीमा', 'मा', 'बढी', 'सबल', 'सुरक्षा']
# test = [{'pos': 'IKM', 'prev-prev-word': 'अधिवेशन', 'word': 'को', 'prev-word': 'आषाढ', 'prev-pos': 'NN', 'next-next-word': 'मा', 'prev-prev-pos': 'NN', 'next-pos': 'NN', 'next-word': 'शुरु', 'nextnextpos': 'II'}]
for x in range(0, len(test)):
    test_feat.append(ExtractFeatures.get_wordFeatures(test, x))
print(test, test_feat)


vec = DictVectorizer(sparse=False)
X_arr = vec.fit_transform(trainFeatures)
print("Converting word features into Numpy arrays")
print(X_arr)
XTest_arr = vec.fit_transform(test_feat)
print("Converting test word features into Numpy arrays")
print(XTest_arr)


print(X_arr.shape[1], XTest_arr.shape[1])
clf = svm.SVC(kernel="linear")
clf.fit(X_arr, trainLabels)

print("Support vectors")
print(clf.support_vectors_)
with open("support.txt", "wb") as f:
    np.savetxt(f, clf.support_vectors_)
    f.close()
print("No of Support Vectors")
print(clf.n_support_)
print("Support vector indices")
print(clf.support_)
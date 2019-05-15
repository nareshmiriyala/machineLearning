from sklearn import tree
#Step 1 Collect Training Data
#Fruits features are Weight and Texture(Bumpy or Smooth)..assumed Texture smooth as 1 and 0 for bumpy
features=[[140,1],[130,1],[150,0],[170,0]]
#Lables are apple or orange,0 for apple and 1 for orange
labels=[0,0,1,1]
#Step 2 : Train Classifier ( Decision Tree)
clf=tree.DecisionTreeClassifier()

#Traning alogirthm
clf.fit(features,labels)

print (clf.predict([[150,0]]))

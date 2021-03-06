import json
data = json.load(open('instances_train2017.json'))

print data.keys()
#OUTPUT :
#  [u'info', u'licenses', u'images', u'annotations', u'categories']

print data['categories']

'''
OUTPUT :
  
[{u'id': 1, u'name': u'person', u'supercategory': u'person'},
 {u'id': 2, u'name': u'bicycle', u'supercategory': u'vehicle'},
 {u'id': 3, u'name': u'car', u'supercategory': u'vehicle'},
 {u'id': 4, u'name': u'motorcycle', u'supercategory': u'vehicle'},
 {u'id': 5, u'name': u'airplane', u'supercategory': u'vehicle'},
 {u'id': 6, u'name': u'bus', u'supercategory': u'vehicle'},
 {u'id': 7, u'name': u'train', u'supercategory': u'vehicle'},
 {u'id': 8, u'name': u'truck', u'supercategory': u'vehicle'},
 {u'id': 9, u'name': u'boat', u'supercategory': u'vehicle'},
 {u'id': 10, u'name': u'traffic light', u'supercategory': u'outdoor'},
 {u'id': 11, u'name': u'fire hydrant', u'supercategory': u'outdoor'},
 {u'id': 13, u'name': u'stop sign', u'supercategory': u'outdoor'},
 {u'id': 14, u'name': u'parking meter', u'supercategory': u'outdoor'},
 {u'id': 15, u'name': u'bench', u'supercategory': u'outdoor'},
 {u'id': 16, u'name': u'bird', u'supercategory': u'animal'},
 {u'id': 17, u'name': u'cat', u'supercategory': u'animal'},
 {u'id': 18, u'name': u'dog', u'supercategory': u'animal'},
 {u'id': 19, u'name': u'horse', u'supercategory': u'animal'},
 {u'id': 20, u'name': u'sheep', u'supercategory': u'animal'},
 {u'id': 21, u'name': u'cow', u'supercategory': u'animal'},
 {u'id': 22, u'name': u'elephant', u'supercategory': u'animal'},
 {u'id': 23, u'name': u'bear', u'supercategory': u'animal'},
 {u'id': 24, u'name': u'zebra', u'supercategory': u'animal'},
 create_data_subset(folder_name='horse_images', category='bicycle')
 
 def create_data_subset(folder_name, category):
  # note this only refers to  the training set and not the validation set
  coco = COCO('annotations/instances_train2017.json')  

  # note this only refers to the captions of the training set and not the validation set   
  caps = COCO('annotations/captions_train2017.json') 

  categories = coco.loadCats(coco.getCatIds())
  names = [cat['name'] for cat in categories] 

  print("Available categories: ")
  for index, n in enumerate(names):
      print(index, n)

  category_ids = coco.getCatIds(catNms=[category])
  image_ids = coco.getImgIds(catIds=category_ids)
  images = coco.loadImgs(image_ids)
  annIds = caps.getAnnIds(imgIds=image_ids)
  annotations = caps.loadAnns(annIds)

  # Split the annotations every 5 captions since there are 5 captions for each image
  annotations = [annotations[x:x + 5] for x in range(0, len(annotations), 5)]

  # Create empty dataframe with two columns for the image file name and the corresponding 
  captions
  df = pd.DataFrame(columns=['image_id', 'caption'])

  # Create folder in for the images of the selected category
  os.mkdir(folder_name)

  # Create map for image id (key) to captions (values)
  captions_dict = {}
  for i, n in enumerate(annotations):
      captions_dict[annotations[i][0]['image_id']] = annotations[i]

  horse_file_names = []
  for img in images:
      horse_file_names.append(img['file_name'])
      for entry in captions_dict[img['id']]:
          df.loc[len(df)] = [img['file_name'], entry['caption']]

  # Convert dataframe to csv file and save to folder
  df.to_csv(folder_name + "/captions.csv", index=False)

  # Copy all images of given category to new folder
  for filename in os.listdir('train2017'):
      if filename in horse_file_names:
          shutil.copy(os.path.join('train2017', filename), folder_name)

  print('Done creating data subset with images....')
 {u'id': 25, u'name': u'giraffe', u'supercategory': u'animal'},
 {u'id': 27, u'name': u'backpack', u'supercategory': u'accessory'},
 {u'id': 28, u'name': u'umbrella', u'supercategory': u'accessory'},
 {u'id': 31, u'name': u'handbag', u'supercategory': u'accessory'},
 {u'id': 32, u'name': u'tie', u'supercategory': u'accessory'},
 {u'id': 33, u'name': u'suitcase', u'supercategory': u'accessory'},
 {u'id': 34, u'name': u'frisbee', u'supercategory': u'sports'},
 {u'id': 35, u'name': u'skis', u'supercategory': u'sports'},
 {u'id': 36, u'name': u'snowboard', u'supercategory': u'sports'},
 {u'id': 37, u'name': u'sports ball', u'supercategory': u'sports'},
 {u'id': 38, u'name': u'kite', u'supercategory': u'sports'},
 {u'id': 39, u'name': u'baseball bat', u'supercategory': u'sports'},
 {u'id': 40, u'name': u'baseball glove', u'supercategory': u'sports'},
 {u'id': 41, u'name': u'skateboard', u'supercategory': u'sports'},
 {u'id': 42, u'name': u'surfboard', u'supercategory': u'sports'},
 {u'id': 43, u'name': u'tennis racket', u'supercategory': u'sports'},
 {u'id': 44, u'name': u'bottle', u'supercategory': u'kitchen'},
 {u'id': 46, u'name': u'wine glass', u'supercategory': u'kitchen'},
 {u'id': 47, u'name': u'cup', u'supercategory': u'kitchen'},
 {u'id': 48, u'name': u'fork', u'supercategory': u'kitchen'},
 {u'id': 49, u'name': u'knife', u'supercategory': u'kitchen'},
 {u'id': 50, u'name': u'spoon', u'supercategory': u'kitchen'},
 {u'id': 51, u'name': u'bowl', u'supercategory': u'kitchen'},
 {u'id': 52, u'name': u'banana', u'supercategory': u'food'},
 {u'id': 53, u'name': u'apple', u'supercategory': u'food'},
 {u'id': 54, u'name': u'sandwich', u'supercategory': u'food'},
 {u'id': 55, u'name': u'orange', u'supercategory': u'food'},
 {u'id': 56, u'name': u'broccoli', u'supercategory': u'food'},
 {u'id': 57, u'name': u'carrot', u'supercategory': u'food'},
 {u'id': 58, u'name': u'hot dog', u'supercategory': u'food'},
 {u'id': 59, u'name': u'pizza', u'supercategory': u'food'},
 {u'id': 60, u'name': u'donut', u'supercategory': u'food'},
 {u'id': 61, u'name': u'cake', u'supercategory': u'food'},
 {u'id': 62, u'name': u'chair', u'supercategory': u'furniture'},
 {u'id': 63, u'name': u'couch', u'supercategory': u'furniture'},
 {u'id': 64, u'name': u'potted plant', u'supercategory': u'furniture'},
 {u'id': 65, u'name': u'bed', u'supercategory': u'furniture'},
 {u'id': 67, u'name': u'dining table', u'supercategory': u'furniture'},
 {u'id': 70, u'name': u'toilet', u'supercategory': u'furniture'},
 {u'id': 72, u'name': u'tv', u'supercategory': u'electronic'},
 {u'id': 73, u'name': u'laptop', u'supercategory': u'electronic'},
 {u'id': 74, u'name': u'mouse', u'supercategory': u'electronic'},
 {u'id': 75, u'name': u'remote', u'supercategory': u'electronic'},
 {u'id': 76, u'name': u'keyboard', u'supercategory': u'electronic'},
 {u'id': 77, u'name': u'cell phone', u'supercategory': u'electronic'},
 {u'id': 78, u'name': u'microwave', u'supercategory': u'appliance'},
 {u'id': 79, u'name': u'oven', u'supercategory': u'appliance'},
 {u'id': 80, u'name': u'toaster', u'supercategory': u'appliance'},
 {u'id': 81, u'name': u'sink', u'supercategory': u'appliance'},
 {u'id': 82, u'name': u'refrigerator', u'supercategory': u'appliance'},
 {u'id': 84, u'name': u'book', u'supercategory': u'indoor'},
 {u'id': 85, u'name': u'clock', u'supercategory': u'indoor'},
 {u'id': 86, u'name': u'vase', u'supercategory': u'indoor'},
 {u'id': 87, u'name': u'scissors', u'supercategory': u'indoor'},
 {u'id': 88, u'name': u'teddy bear', u'supercategory': u'indoor'},
 {u'id': 89, u'name': u'hair drier', u'supercategory': u'indoor'},
 {u'id': 90, u'name': u'toothbrush', u'supercategory': u'indoor'}]
'''

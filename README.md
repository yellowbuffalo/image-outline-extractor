# image-outline-tool
For image processing, the tool is help user to extract the outline as a feature for image processing tasks.(Such as image classification)
* Implement Opencv to handle with the image.
  * Step 1. Gamma correction to brighten the picture.
  * Step 2. Conduct morphology to get the outline of the data.
  * Step 3. Do closing on the picture after morphology to strengthen the object on picture(such as building and mountain) 
* The dataset is come from [Intel Image Classification on Kaggle](https://www.kaggle.com/datasets/puneet6060/intel-image-classification) 

## Usage:
* Using following to build environment
  ```console
  user@bar:~$ python3 -m venv myenv
  user@bar:~$ source myenv/bin/activate
  user@bar:~$ pip3 install -r requirements.txt
  user@bar:~$ python3 example.py
  ```
* The simple usage will like code below:
  ```python
  
  img = cv2.imread('./data/3.jpg')
  img_process = outlineExtractor(img) # Implement the class on image.
  img_process.gammaCorrection() # Conduct the gamma correction to brighten the picture.
  img_process.morphology() # Doing morphology to outline the image.
  cv2.imwrite('./output/gamma/' + target, img_process.img_gamma)  # Output the img after gamma
  cv2.imwrite('./output/outline/' + target, img_process.gradient) # Output the outline
  cv2.imwrite('./output/closing/' + target, img_process.closing)  # Output the img after closing
  
  ```
## Result for example:
### Raw image: 
![Raw image](https://github.com/yellowbuffalo/image-outline-tool/blob/main/data/14.jpg?raw=true)
### Image after gamma correction: 
![Image after gamma correction](https://github.com/yellowbuffalo/image-outline-tool/blob/main/output/gamma/14.jpg?raw=true)
### Image after morphology: 
![Image after morphology](https://github.com/yellowbuffalo/image-outline-tool/blob/main/output/outline/14.jpg?raw=true)
### Image after closing:
![Image after closing](https://github.com/yellowbuffalo/image-outline-tool/blob/main/output/closing/14.jpg?raw=true)


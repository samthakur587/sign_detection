## sign language detection using mediapipe holistic 

I created a sign language detection web app where we can communicate with deaf people. this is the version v-0.1 where I trained a lstm model which can only detected 5 sign.

In order to use this model you can run the following command in your terminal. i am using anconda so this command are only for conda you can also use python environment also.



# step 1 : create new environment in conda 

```bash 

conda create -n new_env
conda activate new_env

```

# step 2  : clone this repository 

```bash

git clone https://github.com/samthakur587/sign_detection.git

```

# step 3  : intall the required dependences by runing this command


```bash 

pip install -r requirement.txt

```

step 4 : Run python file test for making prediction 

```bash

pyhton test.py

```

I have created the custom dataset for this model. and you can also create your custom data by runing this two file make_folder.py and making_data.py for creating data

```bash

python make_data.py
python making_data.py

```
for a good accuracy in lstm model need more data. since i have created custom data of my own its defficult to make it for all sign. so i created only 5 sign for this version v.01 and now i am working on v0.2 which include large set of sign ......................

# [LinkedIn](https://www.linkedin.com/in/samunder-singh/)


# [LICENSE](https://github.com/samthakur587/sign_detection/blob/main/LICENSE.md)


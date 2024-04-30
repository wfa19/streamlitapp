# MyStreamlitApp Documentation

## Overview

MyStreamlitApp is a Streamlit-based web application designed to streamline the machine learning workflow. Users can upload their data, select a target variable, and configure various aspects of the machine learning pipeline, including data preparation, transformation, feature engineering, feature selection, and model training. The app then leverages the PyCaret library to train and tune machine learning models based on the user's configurations.

## Accessing the App

You can access MyStreamlitApp online by visiting the following link:

[MyStreamlitApp](https://appapp-qnebc74f2xhhqkx2s6ypwr.streamlit.app/)

## Usage Instructions

1. Upload Data: Start by uploading your dataset using the provided interface.
2. Select Target Variable: Choose the target variable from the uploaded dataset.
3. Configure ML Pipeline: Use the rendered UI inputs to configure data preparation, transformation, feature engineering, feature selection, and model training settings according to your requirements.
4. Train and Tune Model: Once you've configured the pipeline settings, click the "Train Model" button to initiate model training and tuning using PyCaret.
5. Download Trained Model: After the model training is complete, you can download the trained model for future use.



## Example
### Loading data
![image](https://github.com/wfa19/streamlitapp/assets/85408528/3839544d-59d9-4740-859a-1befc402f729)

### select target
![image](https://github.com/wfa19/streamlitapp/assets/85408528/5d4d668f-12f6-4943-b85c-48dbd4612d3c)

### configure setings

![image](https://github.com/wfa19/streamlitapp/assets/85408528/308e1a96-7913-4c30-b847-ad25636d6636)

![image](https://github.com/wfa19/streamlitapp/assets/85408528/d753e6d5-44b7-40e7-bbc8-90ccad87ccde)

![image](https://github.com/wfa19/streamlitapp/assets/85408528/09392be7-f554-44b7-8724-d8d1cd3c35f9)

![image](https://github.com/wfa19/streamlitapp/assets/85408528/1de6a9f0-1daa-4605-b65a-09157e8fe62b)

## sample outputs
### bargraph 
![image](https://github.com/wfa19/streamlitapp/assets/85408528/c5adb655-9c8c-4da7-b79d-2b792a86e5ce)

### correlation plot
![image](https://github.com/wfa19/streamlitapp/assets/85408528/c5959ac9-c1c8-49e4-91d3-e2b20f4c22ca)
### model set up 
![image](https://github.com/wfa19/streamlitapp/assets/85408528/8fc63ffe-5a26-49e0-8783-75cf45fea1b6)

## performances 
![image](https://github.com/wfa19/streamlitapp/assets/85408528/611c248a-8c2b-419b-ba28-7c028abb5b33)
![image](https://github.com/wfa19/streamlitapp/assets/85408528/6d5c147b-86d6-4421-b89e-e780e034b316)

## Limitations

One limitation of MyStreamlitApp is that every time new data is uploaded through the Streamlit app, the entire app refreshes, leading to the loss of the trained model. This limitation makes it challenging to perform in-app predictions on newly uploaded data. Future enhancements may involve implementing a solution to preserve the trained model state across data uploads, allowing for seamless in-app predictions. Another limitation is the virtual env provided by streamlit is small and may make the process slow. but running from the repo with codeblocks or computer works seamlessly.

## Feedback and Support

If you have any feedback, encounter issues, or have suggestions for improvement while using MyStreamlitApp, please feel free to submit an issue or [submit an issue](https://github.com/yourusername/mystreamlitapp/issues) on GitHub.

## Credits

MyStreamlitApp was developed by Wafa..

## License

This project is licensed under the [MIT License](LICENSE).

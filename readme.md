# Air Quality Index Prediction

## Introduction
Air pollution poses a significant threat to public health and the environment worldwide. Monitoring and predicting air quality is vital for mitigating its adverse effects. Our project aims to develop a robust predictive model for forecasting the Air Quality Index (AQI) using data science techniques.

## Objective
The key objective of our proposal is to develop a precise and user-friendly predictive model for forecasting the Air Quality Index (AQI) using data science techniques. By leveraging the expertise of our multidisciplinary team and a robust dataset including historical air quality measurements, we aim to address the critical need for exact AQI predictions. Our objective is to empower stakeholders, including policymakers, environmentalists, and the general public, with actionable insights to mitigate the adverse effects of air pollution and foster a healthier, more sustainable environment. Through this project, we strive to contribute to improved air quality management and public health awareness initiatives on a global scale.

## Problem Statement
Despite advancements in monitoring technologies, accurately forecasting the Air Quality Index (AQI) remains a significant challenge. Current methods often lack precision and fail to capture the complex interplay of factors influencing air quality. As a result, stakeholders face difficulties in making informed decisions to mitigate the adverse effects of air pollution on public health and the environment. There is a critical need for innovative solutions that leverage data science to develop reliable AQI prediction models. Our project aims to address this pressing issue by creating a user-friendly model capable of forecasting AQI levels accurately, thereby enabling better air quality management and public health interventions.

## Dataset
The ["Air Quality Data Set"](https://archive.ics.uci.edu/dataset/360/air+quality) from the UCI Machine Learning Repository contains air quality measurements collected at an urban traffic intersection in an Italian city. Spanning March 2004 to February 2005, the dataset includes hourly recordings of pollutants like carbon monoxide and nitrogen oxides, alongside meteorological data such as temperature and humidity. With 15 attributes, it offers opportunities for research in air quality forecasting, environmental studies, and machine learning applications. This freely accessible dataset serves as a valuable resource for analyzing the impact of air pollution on public health and developing mitigation strategies.

## Methodology
Our approach involves several key steps:
1. **Data Preprocessing:** Cleaning and preparing the dataset for analysis, handling missing values, and normalizing the data.
2. **Feature Engineering:** Selecting and creating relevant features that influence AQI levels.
3. **Model Development:** Implementing various machine learning models such as Linear Regression, Decision Trees, Random Forest, and Neural Networks.
4. **Model Evaluation:** Assessing the performance of the models using metrics like Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R-squared.
5. **Model Optimization:** Fine-tuning the best-performing model to enhance its predictive accuracy.
6. **Deployment:** Creating a user-friendly interface for stakeholders to easily access and interpret AQI forecasts.

## Results
Through this project, I learned a lot about data science, machine learning, and air quality prediction. The results included accurate AQI predictions and graphical visualizations of the data, which were displayed on a responsive front-end interface.

## Conclusion
This project aims to provide a reliable and accurate AQI prediction model that can assist in effective air quality management. By utilizing advanced data science techniques, we hope to deliver actionable insights that can help mitigate the adverse effects of air pollution on public health and the environment.

## Future Work
Future enhancements could include:
- Expanding the dataset to include more recent and varied geographic data.
- Incorporating additional meteorological and environmental factors.
- Developing real-time AQI prediction capabilities.
- Enhancing the user interface for better accessibility and usability.

## Screenshots
- ![Interface](https://i.imgur.com/BC4zn0k.png)
- ![Predicted Table 1](https://i.imgur.com/row3SZG.png)
- ![Predicted Table 1 Cont](https://i.imgur.com/pyFta1p.png)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- UCI Machine Learning Repository for providing the dataset.
- Developed with the help of online tutorials

## To Run the Project
1. Install Libraries / Dependencies:
    ```sh
    pip install -r requirements.txt
    ```
2. Set directory to:
    ```sh
    > website/
    ```
3. Run the command:
    ```sh
    python app.py
    ```
```
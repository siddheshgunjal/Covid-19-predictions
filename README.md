# Covid-19-predictions

This project is done in response to paritcipate in this hackathon https://www.machinehack.com/course/covid-19-forecasting-the-corona-outbreak/

The main goal was to develop a highly accurate model which can predict the *'Number of Confirmed cases'*, *'Number of death cases'*. in 188 Countries/Regions for the next day.

Final Accuracy ~ 98% | Highest Accuracy achieved = 98.96%

Following libraries are required to run Complete TSA:
 - Numpy
 - Pandas
 - Statsmodels
 - pmdarima (install with *pip*)
 
 To perform predictions on a single Country/Region: `single_country_pred.ipynb` in any suitable notebook.
 
 To explore the varies TSA methods to perform predictions: `exploringother_tsa_methods.ipynb`.
 
 To run the predictions for the next day and generate a submission file with predictions for the next day, run this in cmd/terminal: `python covid19_final.py`

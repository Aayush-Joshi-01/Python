```commandline
.venv) D:\Python\Week-10\11 July\Project_Analysis>python main_interface.py

Welcome to Data Analysis Application
=================================== 
/descriptive for descriptive analysis
/comparative for comparative analysis
/temporal for temporal analysis
/spatial for spatial analysis
/behavioral for behavioral analysis
/health for health metrics analysis
/predictive for predictive analysis
/exit to exit the program

Enter your choice (descriptive/comparative/temporal/spatial/behavioral/health/predictive/exit): /descriptive
Loading data: 100%|████████████████████████████████████████████████████████████████████████████████████████| 1000/1000 [00:06<00:00, 163.08it/s]
Data loaded successfully from Data/fitness_tracker_dataset.csv

Basic Statistics:
              user_id           steps  calories_burned     distance_km  active_minutes     sleep_hours  heart_rate_avg
count  1000000.000000  1000000.000000   1000000.000000  1000000.000000  1000000.000000  1000000.000000  1000000.000000
mean       499.550302    15005.767061      2750.008148        9.994465      719.418241        6.000228      119.458316
std        288.166608     8659.195341       721.473950        5.774298      415.894771        3.463977       34.654034
min          1.000000        0.000000      1500.000000        0.000000        0.000000        0.000000       60.000000
25%        250.000000     7492.000000      2125.517500        4.990000      359.000000        3.000000       89.000000
50%        499.000000    15020.000000      2748.310000        9.990000      719.000000        6.000000      119.000000
75%        749.000000    22507.000000      3375.190000       14.990000     1080.000000        9.000000      149.000000
max        999.000000    29999.000000      4000.000000       20.000000     1439.000000       12.000000      179.000000
Report 'basic_statistics.txt' saved successfully.
Do you want to see the menu again: y  

Welcome to Data Analysis Application
===================================
/descriptive for descriptive analysis
/comparative for comparative analysis
/temporal for temporal analysis
/spatial for spatial analysis
/behavioral for behavioral analysis
/health for health metrics analysis
/predictive for predictive analysis
/exit to exit the program

Enter your choice (descriptive/comparative/temporal/spatial/behavioral/health/predictive/exit): /comparative
Loading data: 100%|████████████████████████████████████████████████████████████████████████████████████████| 1000/1000 [00:05<00:00, 167.21it/s]
Data loaded successfully from Data/fitness_tracker_dataset.csv
Report 'average_calories_by_workout_type.txt' saved successfully.
Loading data: 100%|████████████████████████████████████████████████████████████████████████████████████████| 1000/1000 [00:07<00:00, 134.38it/s]
Data loaded successfully from Data/fitness_tracker_dataset.csv
Report 'correlation_analysis.txt' saved successfully.
Do you want to see the menu again: y

Welcome to Data Analysis Application
===================================
/descriptive for descriptive analysis
/comparative for comparative analysis
/temporal for temporal analysis
/spatial for spatial analysis
/behavioral for behavioral analysis
/health for health metrics analysis
/predictive for predictive analysis
/exit to exit the program

Enter your choice (descriptive/comparative/temporal/spatial/behavioral/health/predictive/exit): /temporal
Loading data: 100%|████████████████████████████████████████████████████████████████████████████████████████| 1000/1000 [00:07<00:00, 134.89it/s] 
Data loaded successfully from Data/fitness_tracker_dataset.csv
Report 'monthly_steps_trend.txt' saved successfully.
Report 'average_steps_by_season.txt' saved successfully.
Do you want to see the menu again: n

Enter your choice (descriptive/comparative/temporal/spatial/behavioral/health/predictive/exit): /spatial
Loading data: 100%|████████████████████████████████████████████████████████████████████████████████████████| 1000/1000 [00:06<00:00, 154.35it/s] 
Data loaded successfully from Data/fitness_tracker_dataset.csv
Report 'average_steps_by_location.txt' saved successfully.
D:\Python\Week-10\11 July\Project_Analysis\Models\data_processor.py:181: UserWarning: Creating legend with loc="best" can be slow with large amounts of data.
  plt.tight_layout()
D:\Python\Week-10\11 July\Project_Analysis\Models\data_processor.py:182: UserWarning: Creating legend with loc="best" can be slow with large amounts of data.
  plt.savefig('Reports/visualizations/activities_by_location.png')
C:\Users\joshi.aayush\AppData\Local\Programs\Python\Python312\Lib\tkinter\__init__.py:861: UserWarning: Creating legend with loc="best" can be slow with large amounts of data.
  func(*args)
Report 'activities_by_location.txt' saved successfully.
Do you want to see the menu again: y

Welcome to Data Analysis Application 
===================================  
/descriptive for descriptive analysis
/comparative for comparative analysis
/temporal for temporal analysis
/spatial for spatial analysis
/behavioral for behavioral analysis
/health for health metrics analysis
/predictive for predictive analysis
/exit to exit the program

Enter your choice (descriptive/comparative/temporal/spatial/behavioral/health/predictive/exit): /behavioral
404 Not Found

Do you want to see the menu again: /behavior

Enter your choice (descriptive/comparative/temporal/spatial/behavioral/health/predictive/exit): /behavior
Loading data: 100%|████████████████████████████████████████████████████████████████████████████████████████| 1000/1000 [00:06<00:00, 163.40it/s]
Data loaded successfully from Data/fitness_tracker_dataset.csv
Report 'average_steps_by_day.txt' saved successfully.
D:\Python\Week-10\11 July\Project_Analysis\Models\data_processor.py:215: FutureWarning: 

Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.

  sns.boxplot(x='weather_conditions', y='steps', data=data, palette='Set2')
Do you want to see the menu again: y

Welcome to Data Analysis Application
===================================
/descriptive for descriptive analysis
/comparative for comparative analysis
/temporal for temporal analysis
/spatial for spatial analysis
/behavioral for behavioral analysis
/health for health metrics analysis
/predictive for predictive analysis
/exit to exit the program

Enter your choice (descriptive/comparative/temporal/spatial/behavioral/health/predictive/exit): /healt
404 Not Found

Do you want to see the menu again: /health

Enter your choice (descriptive/comparative/temporal/spatial/behavioral/health/predictive/exit): /health
Loading data: 100%|████████████████████████████████████████████████████████████████████████████████████████| 1000/1000 [00:06<00:00, 165.91it/s]
Data loaded successfully from Data/fitness_tracker_dataset.csv
D:\Python\Week-10\11 July\Project_Analysis\Models\data_processor.py:237: UserWarning: Creating legend with loc="best" can be slow with large amounts of data.
  plt.tight_layout()
D:\Python\Week-10\11 July\Project_Analysis\Models\data_processor.py:238: UserWarning: Creating legend with loc="best" can be slow with large amounts of data.
  plt.savefig('Reports/visualizations/health_impact_of_activity.png')
C:\Users\joshi.aayush\AppData\Local\Programs\Python\Python312\Lib\tkinter\__init__.py:861: UserWarning: Creating legend with loc="best" can be slow with large amounts of data.
  func(*args)
D:\Python\Week-10\11 July\Project_Analysis\Models\data_processor.py:249: FutureWarning: 

Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.

  sns.barplot(x=avg_heart_rate_by_activity.index, y=avg_heart_rate_by_activity.values, palette='viridis')
Report 'average_heart_rate_by_activity.txt' saved successfully.
Do you want to see the menu again: y

Welcome to Data Analysis Application
===================================
/descriptive for descriptive analysis
/comparative for comparative analysis
/temporal for temporal analysis
/spatial for spatial analysis
/behavioral for behavioral analysis
/health for health metrics analysis
/predictive for predictive analysis
/exit to exit the program

Enter your choice (descriptive/comparative/temporal/spatial/behavioral/health/predictive/exit): /predictive
Loading data: 100%|████████████████████████████████████████████████████████████████████████████████████████| 1000/1000 [00:06<00:00, 163.17it/s]
Data loaded successfully from Data/fitness_tracker_dataset.csv
Mood prediction accuracy: 0.25
Average Steps and Heart Rate by Season:
   season         steps  heart_rate_avg
0       0  15023.146404      119.432894
1       1  15001.260199      119.462529
2       2  14997.677612      119.485264
3       3  15005.190721      119.444513
{'Winter': Empty DataFrame
Columns: [season, steps, heart_rate_avg]
Index: [], 'Spring': Empty DataFrame
Columns: [season, steps, heart_rate_avg]
Index: [], 'Summer': Empty DataFrame
Columns: [season, steps, heart_rate_avg]
Index: [], 'Fall': Empty DataFrame
Columns: [season, steps, heart_rate_avg]
Index: []}
Do you want to see the menu again: n

Enter your choice (descriptive/comparative/temporal/spatial/behavioral/health/predictive/exit): /exit
404 Not Found

Do you want to see the menu again: faux

Enter your choice (descriptive/comparative/temporal/spatial/behavioral/health/predictive/exit): faux
Exiting the program...

```
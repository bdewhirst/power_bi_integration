1. Create environment (here, poetry)
2. Add necessary packages to environment (pandas, numpy, matplotlib)
3. compose and test python script
4. open PowerBI (PBI)

After here, steps are in PBI unless otherwise noted
5. specify python environment python.exe location
6. specify IDE (PyCharm) executable's location
7. add data > other > python > (enter script)
8. adjust data types in data model tab (lower of three icons on left)
9. optionally, indicate whether or not to aggregate
10. build a visual (may need to aggregate values with max or min to disagregate)
11. save, publish, or whatever

12. ran into issues installing scikit-learn (tried to cancel installing wrong version, messed up poetry)
    (resolved by creating alternate conda environment)

ref: https://www.datacamp.com/tutorial/running-python-scripts-in-power-bi-tutorial

from ref:
PowerBI supports:

* Matplotlib (in requirements.txt)
* NumPy (installed implicitly as dependency of packages in requirements.txt)
* Pandas (in requirements.txt)
* Scikit-learn
* Scipy  (installed implicitly as dependency of packages in requirements.txt)
* Seaborn (not yet installed)
* Statsmodels (not yet installed)
* XGBoost (not yet installed)
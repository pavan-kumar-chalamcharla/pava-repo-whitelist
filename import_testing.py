# Databricks notebook source
from testing_folder.sample import n_to_mth
n_to_mth(3, 4)

# COMMAND ----------

testing_folder/sample.py

# COMMAND ----------

from testing_folder.mysql_class import MYSQL
print(MYSQL.PORT)

# COMMAND ----------

from importing_corss_repos.mysql_class import MYSQL
print(MYSQL.PORT)

# COMMAND ----------

import sys
import os
 
# In the command below, replace <username> with your Databricks user name.
sys.path.append(os.path.abspath('/Workspace/Repos/pavan.kumarchalamcharla@databricks.com/kumar'))

# COMMAND ----------

from importing_corss_repos.mysql_class import MYSQL
print(MYSQL.PORT)

# COMMAND ----------

# MAGIC %sh ls /Workspace/Repos/pavan.kumarchalamcharla@databricks.com

# COMMAND ----------

dbutils.widgets.help()

import os

CMD_INSTALL_LIBS = "python -m pip install -r requirements.txt --trusted-host=pypi.python.org --trusted-host=pypi.org --trusted-host=files.pythonhosted.org"
CMD_SET_SPARK_HOME = 'setx SPARK_HOME "{}"'
CMD_SET_PATH = 'setx PATH "%PATH%;%SPARK_HOME%\\bin"'
CMD_RUN_PYSPARK_TEST = "python ./tests/dlake/core/component/test_ispark.py"
print("Install libs with requirements.txt")
os.system(CMD_INSTALL_LIBS)
import pyspark
spark_path = pyspark.__file__.replace("\\__init__.py", "")
print("Run cmd: %s", CMD_SET_SPARK_HOME.format(spark_path))
os.system(CMD_SET_SPARK_HOME.format(spark_path))
print("Run cmd: %s", CMD_SET_PATH)
os.system(CMD_SET_PATH)
print("Run cmd: %s", CMD_RUN_PYSPARK_TEST)
os.system(CMD_RUN_PYSPARK_TEST)
print("DONE!")

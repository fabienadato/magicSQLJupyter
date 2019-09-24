from IPython.core.magic import line_magic, line_cell_magic, Magics, magics_class
import pandasql as ps

@magics_class
class sqlpandas(Magics):

   @line_cell_magic  
   def sql(self, line, cell=None):
       #if cell and line:
       #    raise ValueError("Line must be empty for cell magic", line)
       #from autovizwidget.widget.utils import display_dataframe

       #df_resultsql = ps.sqldf(cell or line, get_ipython().user_ns)
       #return display_dataframe(df_resultsql)
       return ps.sqldf(cell or line, get_ipython().user_ns)

ip = get_ipython()
ip.register_magics(sqlpandas)
from IPython.core.magic import line_magic, line_cell_magic, Magics, magics_class
import pandasql as ps

@magics_class
class sqlpandas(Magics):

   @line_cell_magic  
   def sql(self, line, cell=None):
        if line.strip() != '':
            resdf = ps.sqldf(cell or line, get_ipython().user_ns)
            get_ipython().user_ns[line.strip()] = resdf
            return resdf
        else: 
            return ps.sqldf(cell or line, get_ipython().user_ns)
            

ip = get_ipython()
ip.register_magics(sqlpandas)
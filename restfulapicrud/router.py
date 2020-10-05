# from employeeapi.viewsets import EmployeeViewset
import employeeapi.viewsets as ev
import CM_ACCT_app.views as CmAcctViewset
import CM_DVCE_INVTR_app.views as CmDeceInvterViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employee',ev.EmployeeViewset)
router.register('name',ev.EmployeeViewset_fullname)
router.register('cmdvceinvtr',CmDeceInvterViewset.cmdvceinvtrlist)
router.register('cmdvceinvtrone', CmDeceInvterViewset.cmdvceinvtronerequest)
router.register('cmacct', CmAcctViewset.CmAcctViewset)
# localhost:p/api/employee/5
# GET, POST, PUT, DELETE
# list , retrive
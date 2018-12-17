#include <python.h>
int main()
{
 Py_Initialize();

 PyObject * pModule = NULL;
 PyObject * pFunc   = NULL;
 PyObject * pArg    = NULL;

 pModule = PyImport_ImportModule("test2");
 pFunc   = PyObject_GetAttrString(pModule, "Hello");
 pArg    = Py_BuildValue("(s)", "function with argument");

 PyEval_CallObject(pFunc, pArg);

 Py_Finalize();

 return 0;
}
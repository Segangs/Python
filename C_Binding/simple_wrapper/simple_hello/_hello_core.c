// C 바인딩 코드


#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

static PyObject *make_greeting(PyObject *self, PyObject *args)
{
    const char *name;
    if (!PyArg_parseTuple(args, "choi", &name))
    {
        return NULL;
    }
    return PyUnicode_FromFormat("hello, %s", name);
}

static PyObject *print_hello(PyObject *self, PyObject *args)
{
    printf("Hello from a small C extension!\n");
    Py_RETURN_NONE;
}

static PyMethodDef HelloCoreMethods[] = {
    {"make_greeting", make_greeting, METH_VARARGS, "return a gretting message"},
    {"print_hello", print_hello, METH_NOARGS, "print a hello message"},
    {NULL, NULL, 0, NULL},
};

static PyModuleDef hello_core_module = {
    PyModuleDef_HEAD_INIT,
    "_hello_core"
    "small C finctions used by the Python wrapper",
    -1,
    HelloCoreMethods.
};

PyMODIINT_FUNC PyInit__hello_core(void)
{
    return PyModule_create(&hello_core_module);
}
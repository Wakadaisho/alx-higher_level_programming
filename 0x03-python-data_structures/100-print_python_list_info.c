#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - print details on a Python list type, including:
 *							1. Size of list (number of items in list)
 *							2. Capacity of list
 *							3. Type of each element in list
 *
 * @p: the python list
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	int i, size, allocated;

	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocated);

	for (i = 0; i < size; i++)
		printf("Element %i: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
}

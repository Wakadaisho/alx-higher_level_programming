#include <Python.h>
#include <stdio.h>
#include <string.h>

/**
 * print_python_bytes - print details on a Python byte type, including:
 *							1. size
 *							2. the byte object as a string
 *							3. the first number of bytes (max 10)
 *
 *
 * @p: the Python byte type
 *
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	int bytes, i;
	long int size;
	char *str;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	PyBytes_AsStringAndSize(p, &str, &size);
	bytes = size < 10 ? size + 1 : 10;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", PyBytes_AsString(p));

	printf("  first %d bytes: ", bytes);

	for (i = 0; i < bytes; i++)
		printf("%02x ", str[i] & 0xff);
	printf("\n");
}

/**
 * print_python_list - print details on a Python list type, including:
 *							1. Size of list (number of items in list)
 *							2. Capacity of list
 *							3. Type of each element in list
 *
 * @p: the python list
 *
 * Return: void
 */
void print_python_list(PyObject *p)
{
	int i, size, allocated;
	PyObject *tmp;

	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocated);

	for (i = 0; i < size; i++)
	{
		tmp = PyList_GET_ITEM(p, i);
		printf("Element %i: %s\n", i, tmp->ob_type->tp_name);
		if (strcmp(tmp->ob_type->tp_name, "bytes") == 0)
			print_python_bytes(tmp);
	}
}

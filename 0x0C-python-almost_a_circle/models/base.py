#!/usr/bin/python3

"""
Module base

Contains the class base, that manages an id attribute
To be used by child classes
"""


class Base:
    """Main base class"""

    _nb_objects = 0

    def __init__(self, id=None):
        if (id is not None):
            self.id = id
        else:
            self.__class__._nb_objects += 1
            self.id = self.__class__._nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a dictionary to its JSON string representation

        Args:
            list_dictionaries (list): a dictionary Python object or None

        Return:
            _json (str)
        """
        if (list_dictionaries is None):
            list_dictionaries = []

        import json

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a JSON string representation to a file

        Args:
            list_objs (list): objects inheriting from Rectangle, Square
        """
        filename = "{}.json".format(cls.__name__)

        _json = "[]"
        if (list_objs is not None):
            _json = cls.to_json_string(
                    [obj.to_dictionary() for obj in list_objs])

        with open(filename, "wt", encoding="utf-8") as f:
            f.write(_json)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON representation of a string

        Args:
            json_string(str): list of dictionaries
        """
        import json

        if (json_string is None or len(json_string) == 0):
            return json.loads("[]")

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes set to dictionary

        Args:
            dictionary (dict):Arguments

        Return:
            Rectangle or Square instance
        """
        obj = cls(1, 1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """Create a list of Rectangle, Square instances
        from a JSON string list

        Return:
            list of Rectangle or Square instances
        """
        import json

        filename = "{}.json".format(cls.__name__)

        with open(filename, "r", encoding="utf-8") as f:
            instances = f.read()

        return [cls.create(**obj) for obj in json.loads(instances)]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize object and save to file as CSV

        Args:
            list_objs: objects to save to file as csv
        """
        _csv = ""
        filename = "{}.csv".format(cls.__name__)

        if (list_objs is not None):
            if (cls.__name__ == "Rectangle"):
                for obj in list_objs:
                    _csv += "{},{},{},{},{}\n".format(
                            obj.id,
                            obj.width,
                            obj.height,
                            obj.x,
                            obj.y
                            )
            elif (cls.__name__ == "Square"):
                for obj in list_objs:
                    _csv += "{},{},{},{}\n".format(
                            obj.id,
                            obj.size,
                            obj.x,
                            obj.y
                            )
            else:
                pass

        with open(filename, "wt", encoding="utf-8") as f:
            f.write(_csv)

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize object and save to file as CSV"""
        filename = "{}.csv".format(cls.__name__)

        objs = []

        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                fields = [int(value) for value in line.strip().split(",")]
                # Swap id to correct position
                id = fields[0]
                fields = fields[1:]
                fields.append(id)
                obj = cls(1, 1)
                obj.update(*fields)
                objs.append(obj)

        return objs

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw shapes on a GUI window using Turtle one after the other
        Rectangles first row, Squares second row
        Space of 50 px between each column
        Space of 50 px between the two rows (from biggest height + y offset)

        Args:
            list_rectangles (list): Rectangle objects to draw
            list_squares (list): Square objects to draw
        """
        import turtle

        def draw_quad(t, width, height, x, y, stroke="black", fill="white"):
            """Draw a quadilateral from the current point as start

            Args:
                t (Turlte object): turtle object
                width (int): width of quad in pixels
                height (int): height of quad in pixels
                x: x-axis displacepment of quad in pixels
                y: y-axis displacepment of quad in pixels
                fill: fill color of quad
            """
            # Setup colors
            t.color(stroke, fill)

            # Move to offset position
            t.penup()
            t.setheading(270)
            t.forward(y)
            t.setheading(0)
            t.forward(x)

            # DRAW!!!
            t.pendown()
            t.begin_fill()
            for _ in range(2):
                t.forward(width)
                t.right(90)
                t.forward(height)
                t.right(90)
            t.end_fill()
            t.penup()

        screen = turtle.Screen()
        width, height = screen.window_width(), screen.window_height()
        t = turtle.Turtle()
        t.speed(10)
        max_height = 0      # largest shape height in row to get spacing
        current_width = 0   # track with to go back to start on next row
        x_buffer = 10       # space between shapes
        y_buffer = 10       # space between rows

        # Go to canvas top left (2px buffer to see edge stroke)
        t.penup()
        t.forward(2)
        t.setheading(180)
        t.forward(width/2)
        t.right(90)
        t.forward(height/2)
        t.back(2)
        t.right(90)

        # Draw the rectangles
        for r in list_rectangles:
            draw_quad(t, r.width, r.height, r.x, r.y)
            max_height = max(max_height, r.height + r.y)
            current_width += r.width + x_buffer + r.x
            t.forward(r.width + x_buffer)

        # Go back to starting column on next row
        t.setheading(180)
        t.forward(current_width)
        current_width = 0
        t.setheading(270)
        t.forward(max_height + y_buffer)
        t.setheading(0)

        # Draw the squares
        for r in list_squares:
            draw_quad(t, r.width, r.height, r.x, r.y)
            max_height = max(max_height, r.height + r.y)
            current_width += r.width + x_buffer + r.x
            t.forward(r.width + x_buffer)

        t.hideturtle()
        turtle.exitonclick()
        turtle.done()

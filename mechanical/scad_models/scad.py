"""SCAD.

# Introduction

This module provides a Python interface to OpenSCAD.

The basic class tree is:

* P: Generic point
  * P2D: 2-dimensional Point
  * P2D: 3-dimensional Point
* Scad: Basic Scad Command
  * Scad2D: 2-dimensional Objects
    * Circle: A circle
    * Square: Rectangle
    * SimplePolygon: Contructed of line segments and arc.
    * Polygon: A SimplePolygon with multiple SimplePolygon holes.
    * LinearExtrude: Linear extrusion of SCAD2D object
    * RotateExtrude: Rotational extrusion of SCAD2D object
  * Scad3D:
    *
  * Transformations:

"""

# MIT License
#
# Copyright (c) 2019 Wayne C. Gramlich (Wayne@Gramlich.Net)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# <----------------------------------------100 Characters----------------------------------------> #

# Import stuff from other libraries:
from math import atan2, ceil, cos, degrees, pi, sin, sqrt
from typing import Any, Callable, IO, List, Optional, Tuple


# P3D:
class P3D:
    """Represents a 3 dimensional point."""

    # P3D.__init__():

    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0) -> None:
        """Initialize the point contents."""
        # Load values into *p3d* (i.e. *self*):
        # p3d: P3D = self
        self.x: float = x
        self.y: float = y
        self.z: float = z

    # P3D.__add__():
    def __add__(self, p3d2: "P3D") -> "P3D":
        """Add two points together."""
        # Use *p3d1* instead of *self*:
        p3d1: P3D = self
        return P3D(p3d1.x + p3d2.x, p3d1.y + p3d2.y, p3d1.z + p3d2.z)

    # P3D.__mul__():
    def __mul__(self, scale: float) -> "P3D":
        """Multiply a p3d by a scale factor."""
        # Use *p3d* instead of *self*:
        p3d: P3D = self
        return P3D(p3d.x * scale, p3d.y * scale, p3d.z * scale)

    # P3D.__rmul__():
    def __rmul__(self, scale: float) -> "P3D":
        """Multiply a p3d by a scale factor."""
        # Use *p3d* instead of *self*:
        p3d: P3D = self
        return P3D(p3d.x * scale, p3d.y * scale, p3d.z * scale)

    # P3D.__sub__():
    def __sub__(self, p3d2: "P3D") -> "P3D":
        """Subtract two p3ds from one another."""
        # Use *p3d1* instead of *self*:
        p3d1: P3D = self
        return P3D(p3d1.x - p3d2.x, p3d1.y - p3d2.y, p3d1.z - p3d2.z)

    # P3D.__str__():
    def __str__(self) -> str:
        """Convert a p3d to a string."""
        # Use *p3d* instead of *self*:
        p3d: P3D = self
        x_text: str = "{0:.3f}".format(p3d.x)
        y_text: str = "{0:.3f}".format(p3d.y)
        z_text: str = "{0:.3f}".format(p3d.z)
        x_text = "0.000" if x_text == "-0.000" else x_text
        y_text = "0.000" if y_text == "-0.000" else y_text
        z_text = "0.000" if z_text == "-0.000" else z_text
        return f"P3D({x_text},{y_text},{z_text})"

    # P3D.__truediv__():
    def __truediv__(self, scale: float) -> "P3D":
        """Divide a p3d by a scale factor."""
        p3d: P3D = self
        return P3D(p3d.x / scale, p3d.y / scale, p3d.z / scale)

    # P3D.distance():
    def distance(self, p3d2) -> float:
        """Compute the distance between two p3ds."""
        p3d1: P3D = self
        dx: float = p3d1.x - p3d2.x
        dy: float = p3d1.y - p3d2.y
        dz: float = p3d1.z - p3d2.z
        return sqrt(dx * dx + dy * dy + dz * dz)


# P2D:
class P2D:
    """Represents a point in 2 demensions."""

    # P2D.__init__():
    def __init__(self, x: float, y: float):
        """Initialize a P2D."""
        # Load *x* and *y* into *p2d* (i.e. *self*):
        # p2d: P2D = self
        self.x: float = x
        self.y: float = y

    # P2D.__add__():
    def __add__(self, p2d2: "P2D") -> "P2D":
        """Add two two P2D's together."""
        # Use *p2d1* instead of *self*:
        p2d1: P2D = self
        return P2D(p2d1.x + p2d2.x, p2d1.y + p2d2.y)

    # P2D.__mul__():
    def __mul__(self, scale: float) -> "P2D":
        """Multiply a P2D by a scale factor."""
        # Use *p2d* instead of *self*:
        p2d: P2D = self
        return P2D(p2d.x * scale, p2d.y * scale)

    # P2D.__rmul__():
    def __rmul__(self, scale: float) -> "P2D":
        """Multiply a P2D by a scale factor."""
        # Use *p2d* instead of *self*:
        p2d: P2D = self
        return P2D(p2d.x * scale, p2d.y * scale)

    # P2D.__sub__():
    def __sub__(self, p2d2: "P2D") -> "P2D":
        """Subtract two P2D's from one another."""
        # Use *p2d1* instead of *self*:
        p2d1: P2D = self
        return P2D(p2d1.x - p2d2.x, p2d1.y - p2d2.y)

    # P2D.__str__():
    def __str__(self) -> str:
        """Convert a P2D to a string."""
        # Use *p2d* instead of *self*:
        p2d: P2D = self
        x_text: str = "{0:.3f}".format(p2d.x)
        y_text: str = "{0:.3f}".format(p2d.y)
        x_text = "0.000" if x_text == "-0.000" else x_text
        y_text = "0.000" if y_text == "-0.000" else y_text
        return f"P2D({x_text},{y_text})"

    # P2D.__truediv__():
    def __truediv__(self, scale: float) -> "P2D":
        """Divide a P2D by a scale factor."""
        p2d: P2D = self
        return P2D(p2d.x / scale, p2d.y / scale)

    # P2D.distance():
    def distance(self, p2d2: "P2D") -> float:
        """Compute the distance between two P2D's."""
        p2d1: P2D = self
        dx: float = p2d1.x - p2d2.x
        dy: float = p2d1.y - p2d2.y
        return sqrt(dx * dx + dy * dy)

    # P2D.rotate():
    def rotate(self, angle: float, center: "Optional[P2D]" = None) -> "P2D":
        """Rotate a P2D by angle around the origin."""
        # To rotate a *p2d* (i.e. self) around the origin, use the following formula:
        #
        #   x' = x * cos(angle) - y * sin(angle)
        #   y' = y * cos(angle) + x * sin(angle)
        p2d: P2D = self
        center_x: float
        center_y: float
        if center is None:
            center_x = 0.0
            center_y = 0.0
        else:
            center_x = center.x
            center_y = center.y
        x: float = p2d.x - center_x
        y: float = p2d.y - center_y
        sin_angle: float = sin(angle)
        cos_angle: float = cos(angle)
        rotated_x: float = center_x + x * cos_angle - y * sin_angle
        rotated_y: float = center_y + y * cos_angle + x * sin_angle
        rotated_point: P2D = P2D(rotated_x, rotated_y)
        return rotated_point

    # PD2.y_mirror():
    def y_mirror(self) -> "P2D":
        """Return the p3d mirrored across the Y axis."""
        p2d: P2D = self
        return P2D(-p2d.x, p2d.y)


# Scad:
class Scad:
    """Base class that an OpenSCAD object, transform, etc.

    This base class basically just provides a name and is sub-classed to
    provide all of the functiontality.
    """

    # Scad.__init__()
    def __init__(self, name: str) -> None:
        """Create the base *Scad* object.

        Args:
            *name* (*str*): The name of the *Scad* object.

        """
        # Stuff *name* into the *scad* object (i.e. *self*):
        self.name: str = name

    # Scad.file_write():
    def file_write(self, scad_file: IO[Any]) -> None:
        """Write out a `.scad` file.

        Args:
            *scad_file* (*IO*[*Any*]):
                An IO object (usually to the file system) that can be
                written to.

        """
        # Grab some values from *scad* (i.e. *self*):
        scad: Scad = self
        name: str = scad.name

        # Store the contents of *scad* as a bunch of *scad_lines*:
        scad_lines: List[str] = list()
        scad_lines.append(f"// '{name}' File")
        scad.scad_lines_append(scad_lines, "")

        # Convert *scad_lines* into *scad_text*:
        scad_lines.append("")
        scad_text: str = '\n'.join(scad_lines)

        # Output *scad_text* to *scad_file*:
        assert scad_file.writable(), f"Unable to write out .scad for '{name}'"
        scad_file.write(scad_text)

    # Scad.float_format():
    @staticmethod
    def float_format(value: float) -> str:
        """Convert a float into a string."""
        value_text: str = "{0:.3f}".format(value)
        value_text = "0.000" if value_text == "-0.000" else value_text
        return value_text

    # Scad.polygon_scad_lines_append():
    def polygon_scad_lines_append(self, simple_polygons: "List[SimplePolygon]",
                                  scad_lines: List[str], indent: str) -> None:  # pragma: no cover
        """`Polygon` template command to a list of lines."""
        # Grab *class_name* from *scad* (i.e *self*) and fail with a reasonable error message:
        scad: Scad = self
        class_name: str = scad.__class__.__name__
        assert False, f"{class_name}.polygon_scad_lines_append() is not implemented yet."

    # Scad.scad_lines_append():
    def scad_lines_append(self, scad_lines: List[str], indent: str) -> None:  # pragma: no cover
        """Place holder for virtual *scad_lines_append* method."""
        scad: Scad = self
        class_name: str = scad.__class__.__name__
        assert False, f"{class_name}.scad_lines_append() not implemented yet"


# Scad2D:
class Scad2D(Scad):
    """Represents 2-dimensional Scad objects."""

    # Scad2D.__init__():
    def __init__(self, name: str) -> None:
        """Set the name of the 2-dimensional SCAD object."""
        super().__init__(name)

    # Scad2D.polygon_scad_lines_append():
    def polygon_scad_lines_append(self, simple_polygons: "List[SimplePolygon]",
                                  scad_lines: List[str], indent: str) -> None:
        """Append an OpenSCAD `polygon` command as a list of lines.

        Args:
            *simple_polygons* (*List*[*SimplePolygon*]): A list of
                *SimplePolygon*'s where the first one is the outer
                perimiter of the polygon, and the remaining
                *SimplePolygon*'s are "hole" inside of the outer
                polygon perimeter.  None of these *SimplePolygon*'s
                are allowed to overlap in any way.
            *scad_lines* (*List*[*str*]): A list of strings to which
                individual lines of OpenSCAD code are appended.
            *indent* (*str*): The indentation text to prefixe each
                line with.

        """
        # Grab the *class_name* from *scad2d* (i.e. *self*):
        scad2d: Scad2D = self
        scad_name: str = scad2d.name
        scad_class_name: str = scad2d.__class__.__name__

        # Sweep through all of *simple_polygon*'s and compute *maximum_convexity* and
        # *all_points_size*:
        maximum_convexity: int = 1
        all_points_size: int = 0
        simple_polygon: SimplePolygon
        for simple_polygon in simple_polygons:
            assert simple_polygon.is_locked()
            convexity: int = simple_polygon.convexity
            maximum_convexity = max(maximum_convexity, convexity)
            all_points_size += len(simple_polygon)

        # This code outputs an OpenSCAD `polygon` command in following format:
        #
        #     polygon(points = [ // Begin CLASS_NAME 0-TOTAL_POINTS
        #      // POLYGON1_CLASS 'POLYGON1_NAME' START_INDEX-END_INDEX
        #       [x1, y1], ... , [xN, yN]  // INDEX_RANGE
        #      // POLYGON2_CLASS 'POLYGON2_NAME' START_INDEX-END_INDEX
        #       [x1, y1], ... , [xN, yN]  // INDEX_RANGE
        #      ...
        #      // POLYGONn_CLASS 'POLYGONn_NAME' START_INDEX-END_INDEX
        #       [x1, y1], ... , [xN, yN]  // INDEX_RANGE
        #      ], paths = [
        #       // POLYGON1_CLASS 'POLYGON1_NAME' START_INDEX-END_INDEX
        #       [[x1, y1], ... , [xN, yN]],  // INDEX_RANGE
        #       // POLYGON2_CLASS 'POLYGON2_NAME' START_INDEX-END_INDEX
        #       [[x1, y1], ... , [xN, yN]],  // INDEX_RANGE
        #       ...
        #       // POLYGONn_CLASS 'POLYGONn_NAME' START_INDEX-END_INDEX
        #       [[x1, y1], ... , [xN, yN]  // INDEX_RANGE
        #      ], convexity=CONVEXITY; // End CLASS_NAME 0-TOTAL_POINTS

        # Now start the output of the OpenScad `polygon` command:
        scad_lines.append(f"{indent}polygon(points = [  // Begin {scad_class_name} "
                          f"'{scad_name}' {0}:{all_points_size-1}")

        # Define some variables and constants (alphabetical order):
        float_format: Callable[[float], str] = Scad.float_format
        indices_slice_size: int = 10
        points_slice_size: int = 4
        polygon_class_name: str
        polygon_name: str
        slice_begin_index: int
        slice_end_index: int
        slice_index: int
        slice_last_index: int
        slices_count: int
        simple_polygon_size: int
        simple_polygons_size: int = len(simple_polygons)
        simple_polygon_last_index = simple_polygons_size - 1

        # Step 1: Output all of the points first:
        begin_index: int = 0
        end_index: int
        for simple_polygon_index, simple_polygon in enumerate(simple_polygons):
            # Output the *simple* polygon name and its index range:
            simple_polygon_size = len(simple_polygon)
            end_index = begin_index + simple_polygon_size - 1
            simple_polygon_name = simple_polygon.name
            simple_polygon_class_name = simple_polygon.__class__.__name__
            last_simple_polygon: bool = simple_polygon_index == simple_polygon_last_index
            scad_lines.append(f"{indent} // {simple_polygon_class_name} '{simple_polygon_name}' "
                              f"{begin_index}-{end_index}")

            # Now output 1 or more rows of *points* from *simple_polygon*, truncating to
            # *point_slice_size* to prevent excessively long lines in the `.scad` file:
            points: List[P2D] = simple_polygon.points_get()
            slices_count = int((ceil(float(simple_polygon_size) / float(points_slice_size))))
            slice_last_index = slices_count - 1
            for slice_index in range(slices_count):
                # Extract the *slice* of points from *points*:
                slice_begin_index = slice_index * points_slice_size
                slice_end_index = min(slice_begin_index + points_slice_size, simple_polygon_size)
                slice: List[P2D] = list(points[slice_begin_index:slice_end_index])

                # Figure out all of the text to output for the *slice*:
                point: P2D
                points_text: str = ", ".join([f"[{float_format(point.x)}, {float_format(point.y)}]"
                                              for point in slice])
                end_text: str = ("" if last_simple_polygon and slice_index == slice_last_index
                                 else ",")

                # Perform the append to *scad_lines*:
                scad_lines.append(f"{indent}  {points_text}{end_text}  "
                                  f"// {slice_begin_index}-{slice_end_index}")

            # Update *begin_index* for the next batch of *points* from the next *simple_polygon*:
            begin_index += simple_polygon_size

        # Step 2: Output all of the indices second:
        scad_lines.append(f"{indent} ], paths = [")
        begin_index = 0
        for simple_polygon_index, simple_polygon in enumerate(simple_polygons):
            # Output the *simple* polygon name and its index range:
            simple_polygon_size = len(simple_polygon)
            end_index = begin_index + simple_polygon_size - 1
            simple_polygon_name = simple_polygon.name
            simple_polygon_class_name = simple_polygon.__class__.__name__
            scad_lines.append(f"{indent}  // {simple_polygon_class_name} '{simple_polygon_name}' "
                              f"{begin_index}-{end_index}")
            last_polygon = simple_polygon_index == simple_polygon_last_index

            slices_count = int((ceil(float(simple_polygon_size) / float(indices_slice_size))))
            slice_last_index = slices_count - 1
            for slice_index in range(slices_count):
                slice_begin_index = slice_index * indices_slice_size
                slice_end_index = min(slice_begin_index + indices_slice_size, simple_polygon_size)
                indices: List[str] = [str(begin_index + slice_index)
                                      for slice_index in range(slice_begin_index, slice_end_index)]
                indices_text: str = ", ".join(indices)
                begin_text: str = "[" if slice_index == 0 else " "
                end_text = ("," if slice_index < slices_count - 1
                            else (f"]" if last_polygon else "],"))
                scad_lines.append(f"{indent}  {begin_text}{indices_text}{end_text}")

            # Update *begin_index* for the next batch of *points* for the next *simple_polygon*:
            begin_index += simple_polygon_size

        # Close out the paths and output the *maximum_convexity*:
        scad_lines.append(f"{indent} ], convexity={maximum_convexity});  "
                          f"// End {scad_class_name} '{scad_name}' {0}:{all_points_size-1}")

        # Output the ending debugging comment:
        scad_lines.append(f"{indent}")


# SimplePolygon:
class SimplePolygon(Scad2D):
    """Represents a simple closed polygon of points."""

    # SimplePolygon.__init__():
    def __init__(self, name: str, points: List[P2D] = [],
                 lock: bool = False, convexity: int = -1) -> None:
        """Initialize a SimplePolygon.

        Args:
            *name* (*str*): The name for the polygon.
            *points* (*List*[*P2D*]): The list of points to initialize
                *close_polygon* (i.e. *self* with.)
            *lock* (*bool*): If *True* no additional points can be
                appended to *simple_polygon* (*i.e. *self*); othewise
                additional points can be appended.
            *convexity* (*int*): Specifies the complexity of the
                polygon.  Larger numbers are needed render ever
                complex polygons.  The default is -1, which cause
                a reasonable initial guess to occur.

        """
        # Stuff values into *simpl_polygon* (i.e. *self*):
        # simple_polygon: SimplePolygon = self
        self.locked: bool = lock
        self.name: str = name
        self.points: List[P2D] = points[:]  # Copy the contents of *points*
        self.convexity: int = 4 if convexity <= 0 else convexity

    # SimplePolygon.__getitem__():
    def __getitem__(self, index: int) -> P2D:
        """Fetch a point from the SimplePolygon.

        Args:
            *index* (*int*): Index into the *simple_polygon*
                (i.e. *self*) points list.

        Returns:
            (*P2D*): Return the *index*'th *P2D* from *simple_polygon*.

        """
        # Grab some values from *simple_polygon* (i.e. *self*):
        simple_polygon: SimplePolygon = self
        points: List[P2D] = simple_polygon.points
        points_size: int = len(points)
        if index < 0 or index >= points_size:
            raise IndexError(f"index of {index} is not in range 0 to {points_size-1}")
        point: P2D = points[index]
        return point

    # SimplePolygon.__len__():
    def __len__(self) -> int:
        """Return the number of points currently in the Polygon."""
        # Grab some values from *simple_polygon* (i.e. *self*):
        simple_polygon: SimplePolygon = self
        points: List[P2D] = simple_polygon.points
        size: int = len(points)
        return size

    # SimplePolygon.__str__():
    def __str__(self):
        """Return a short string representation of a Polygon."""
        # Grab some values from *simplepolygon* (i.e. *self*):
        simple_polygon: SimplePolygon = self
        name: str = simple_polygon.name
        points: List[P2D] = simple_polygon.points
        selected_points: List[P2D] = points if len(points) <= 2 else [points[0]] + [points[-1]]
        join_text: str = ", " if len(points) <= 2 else ", ..., "
        selected_point: P2D
        selected_point_texts: List[str] = [f"{selected_point}"
                                           for selected_point in selected_points]
        selected_points_text = join_text.join(selected_point_texts)
        return f"SimplePolygon('{name}', [{selected_points_text}])"

    # SimplePolygon.arc():
    def arc_append(self, center: P2D, radius: float, start_angle: float, end_angle: float,
                   points_count: int) -> None:
        """Append an arc of points to a Polygon.

        Args:
            *origin* (*P*): The center of the arc.
            *radius* (*float*): The arc radius.
            *start_angle* (*float*): The starting angle for the arc.
            *end_angle* (*float*): The ending angle for the arc.
            *points_count* (*int*): The number of points along the arc.

        """
        # Grab some values from *simple_polygon* (i.e. *self*):
        simple_polygon: SimplePolygon = self
        points: List[P2D] = simple_polygon.points

        # Compute the total angle spanned and the delta angle increments:
        span_angle: float = end_angle - start_angle
        delta_angle: float = span_angle / float(points_count - 1)
        # print(f"start_angle={start_angle}={degrees(start_angle)}deg")
        # print(f"end_angle={end_angle}={degrees(end_angle}deg")
        # print(f"span_angle={span_angle}={degrees(span_angle)}deg")
        # print(f"delta_angle={delta_angle}={degrees(delta_angle}deg")
        center_x: float = center.x
        center_y: float = center.y
        index: int
        for index in range(points_count):
            angle: float = start_angle + index * delta_angle
            x: float = center_x + radius * cos(angle)
            y: float = center_y + radius * sin(angle)
            # print(f"[{index}]angle={degrees(angle} x={x} y={y}")
            points.append(P2D(x, y))

    # SimplePolygon.is_locked():
    def is_locked(self) -> bool:
        """Return whether SimplePolygon is locked or not."""
        # Grab *locked* flag from *simple_polygon* (i.e. *self*) and return it:
        simple_polygon: SimplePolygon = self
        locked: bool = simple_polygon.locked
        return locked

    # SimplePolygon.lock():
    def lock(self) -> None:
        """Force SimplePolygon to be locked."""
        simple_polygon: SimplePolygon = self
        simple_polygon.locked = True

    # SimplePolygon.point_append():
    def point_append(self, point: P2D) -> None:
        """Append a point to a SimplePolygon.

        Args:
            *point* (*P2D*): The 2-dimensional point to the
            to *simple_polygon* (i.e. *self*.)

        Raises:
            *ValueError*(*str*): if *simple_polygon* (i.e. *self*.)
            is locked.

        """
        # Grab *points* from *simple_polygon* (i.e. *self*) and tack *point* onto the end:
        simple_polygon: SimplePolygon = self
        points: List[P2D] = simple_polygon.points
        points.append(point)

    # Scad.points_get():
    def points_get(self) -> List[P2D]:
        """Return the points associated with SimplePolygon."""
        simple_polygon: SimplePolygon = self
        points: List[P2D] = simple_polygon.points
        # Make a copy:
        points = list(points[:])
        return points

    # SimplePolygon.points_rotoate():
    def points_rotate(self, angle: float, center: P2D):
        """Rotate all SimplePolygon points by an angle."""
        # Grab some values from *simple_polygon* (i.e. *self*):
        simple_polygon: SimplePolygon = self
        locked: bool = simple_polygon.locked
        points: List[P2D] = simple_polygon.points
        if locked:
            raise ValueError(f"'{simple_polygon.name}' is locked")
        index: int
        point: P2D
        for index, point in enumerate(points):
            points[index] = point.rotate(angle, center)

    # SimplePolygon.points_scad_lines_append():
    def points_scad_lines_append(self, scad_lines: List[str], indent: str, start_index: int) -> int:
        """Append the Polygon points to a list of lines.

        Args:
            *scad_lines* (*List*[*str*]): The list of OpenSCAD lines to
                append to.
            *indent (*str): The indentation text to prefix to each line.
            *start_index* (*int*): The starting index for points.

        Returns:
            (*int*) Returns the *end_index* after the points have been
                output.

        """
        # Grab some values from *simple_polygon* (i.e. *self*):
        simple_polygon: SimplePolygon = self
        name: str = simple_polygon.name
        points: List[P2D] = simple_polygon.points

        # Compute *end_index* from *start_index* and *points_size*:
        points_size: int = len(points)
        end_index: int = start_index + points_size

        # Figure out the number of *slice_points* to output:
        slice_size: int = 4
        slices_count: int = int(ceil(float(points_size) / float(slice_size)))

        # Append a debugging line:
        scad_lines.append(f"{indent} // Polygon '{name}' {start_index}:{end_index-1}")

        # Sweep through *points* and output chunks of *slice_points*:
        slice_index: int
        for slice_index in range(slices_count):
            # Extract the next chunk of *slice_points*:
            slice_start: int = slice_index * slice_size
            slice_end: int = min((slice_index + 1) * slice_size, points_size)
            slice_points: List[P2D] = points[slice_start:slice_end]

            # Just to be paranoid, make sure we actually have at least one point:
            if slice_points:
                # Splice *splice_point* together as a comma separated list:
                point_texts: List[str] = []
                slice_point: P2D
                for slice_point in slice_points:
                    x_text: str = "{0:.3f}".format(slice_point.x)
                    y_text: str = "{0:.3f}".format(slice_point.y)
                    x_text = "0.000" if x_text == "-0.000" else x_text
                    y_text = "0.000" if y_text == "-0.000" else y_text
                    point_texts.append(f"[{x_text}, {y_text}]")
                slice_text: str = ', '.join(point_texts)
                scad_lines.append(f"{indent}  {slice_text}, "
                                  f"// {start_index + slice_start}:"
                                  f"{start_index + slice_end - 1}")
        return end_index

    # SimplePolygon.scad_lines_append():
    def scad_lines_append(self, scad_lines: List[str], indent: str) -> None:
        """TODO."""
        # Grab *class_name* from *simple_polygon* (i.e. *self*):
        simple_polygon: SimplePolygon = self

        # Use the parent *Scad2D*.*scad_lines_append* method to actually ouput the OpenSCAD
        # `polygon` command:
        super().polygon_scad_lines_append([simple_polygon], scad_lines, indent)

    # SimplePolygon.slot_append():
    def slot_append(self, end_point1: P2D, end_point2: P2D,
                    slot_length: float, slot_width: float, points_count: int) -> None:
        """Append a slot to a SimplePolygon.

        *end_point1* and *end_point2* define a line that the slot will
        be alinged with.  The center point between *end_point1* and
        *end_point2* is the center of the slot.  *slot_length* and
        *slot_width* specify the dimensions of the slot.

        Args:
            *end_point1* (*P*): One end point on the center-line of the
                slot.
            *end_point2* (*P*): The other end point on the center-line
                of the slot.
            *slot_length* (*float*): Specifies the overall length of
                the slot.
            *slot_width* (*float*): Specifies the width of the slot.
            *points_count* (*int*): Specifies the number of points
                to use to draw the rounded slot ends.

        """
        # Compute the *center* and *slot_angle* in radians:
        center: P2D = (end_point1 + end_point2) / 2.0
        slot_angle: float = atan2(end_point1.y - end_point2.y, end_point1.x - end_point2.x)

        # Compute the two arc centers:
        slot_radius: float = slot_width / 2.0
        half_slot_length: float = slot_length / 2.0
        degrees180: float = pi
        center1: P2D = P2D(center.x + half_slot_length * cos(slot_angle),
                           center.y + half_slot_length * sin(slot_angle))
        center2: P2D = P2D(center.x + half_slot_length * cos(slot_angle + degrees180),
                           center.y + half_slot_length * sin(slot_angle + degrees180))

        # Append the two slot arcs to *simple_polygon* (i.e. *self*):
        simple_polygon: SimplePolygon = self
        degrees90: float = pi / 2.0
        simple_polygon.arc_append(center1, slot_radius,
                                  slot_angle - degrees90,
                                  slot_angle + degrees90, points_count)
        simple_polygon.arc_append(center2, slot_radius,
                                  slot_angle + degrees180 - degrees90,
                                  slot_angle + degrees180 + degrees90, points_count)

    # SimplePolygon.y_mirror():
    def y_mirror(self) -> "SimplePolygon":
        """Return a copy Y axis mirrored polygon."""
        # Grab some values from *simple_polygon* (i.e. *self*):
        simple_polygon: SimplePolygon = self
        name: str = simple_polygon.name
        points: List[P2D] = simple_polygon.points
        point: P2D
        mirrored_points: List[P2D] = [P2D(-point.x, point.y) for point in points]
        mirrored_polygon: SimplePolygon = SimplePolygon(f"Y-Mirror {name}",
                                                        mirrored_points, lock=True)
        return mirrored_polygon


# Circle:
class Circle(SimplePolygon):
    """Represents a circular SimplePolygon."""

    # Circle.__init__():
    def __init__(self, name: str, diameter: float, points_count: int,
                 center: P2D = P2D(0.0, 0.0)) -> None:
        """Create a circular SimplePolygon.

        Args:
            *name* (*str*): The debugging text name to output to the
                `.scad` file
            *diameter* (*float*): The diameter of the circle.,
            *points_count* (*int*): The number of points to approixmate
                the circle with.
            *center* (*P2D*): The center of the circle.  This defaults
                to the origin (i.e. *P2D*(0.0, 0.0).)

        """
        # Create the *radius *of *circle_points* list of *P2D*'s centered around *center*:
        center_x: float = center.x
        center_y: float = center.y
        radius: float = diameter / 2.0
        circle_points: List[P2D] = []
        delta_angle: float = (2 * pi) / float(points_count)
        point_index: int
        for point_index in range(points_count):
            angle: float = float(point_index) * delta_angle  # Radians
            x: float = center_x + radius * cos(angle)
            y: float = center_y + radius * sin(angle)
            circle_point: P2D = P2D(x, y)
            circle_points.append(circle_point)

        # Initialize the *SimplePolygon* parent class with *name* and *cicular_points*
        # and *lock* it:
        super().__init__(name, circle_points, lock=True)

        # Load values into *circle* (i.e. *self*):
        # circle: Circle = self
        self.center: P2D = center
        self.diameter: float = diameter
        self.points_count: int = points_count
        self.convexty: int = 4

    def __str__(self) -> str:
        """Return a string representation of Circle*."""
        # Grab some values from *Circle* (i.e. *self*):
        circle: Circle = self
        center: P2D = circle.center
        convexity: int = circle.convexity
        diameter: float = circle.diameter
        name: str = circle.name
        points_count: int = circle.points_count

        # Return the formatted string reprentation:
        return f"Circle('{name}',{diameter},{points_count},{center},{convexity})"

    # Circle.key():
    def key(self) -> Tuple[Any]:
        """Return an immutable sorting key for a Circle."""
        # Grab some values from *circle* (i.e. *self*):
        circle: Circle = self
        center: P2D = circle.center
        diameter: float = circle.diameter
        name: str = circle.name

        # (TYPE, NAME, CENTER_X, CENTER_Y, DX, DY, ROTATE):
        key: Any[Tuple] = ("Circle", name, center.x, center.y, diameter, diameter, 0.0)
        return key

    # Circle.scad_lines_append():
    def scad_lines_append(self, scad_lines: List[str], indent: str) -> None:
        """Append Circle to lines list.

        Args:
            *scad_lines* (*List*[*str*]): The lines list to append the
                *circle* (i.e. *self*) to.
            *indent* (*str*): The indentatation prefix for each line.

        """
        # Grab some values from *circle* (i.e. *self*):
        circle: Circle = self
        center: P2D = circle.center
        diameter: float = circle.diameter
        points_count: int = circle.points_count
        name: str = circle.name

        # Derives some values:
        center_x: float = center.x
        center_y: float = center.y
        float_format: Callable[[float], str] = Scad.float_format
        circle_indent: str = indent
        if abs(center_x) != 0.0 or abs(center_y) != 0.0:
            # We have to output a translate transform first:
            scad_lines.append(f"{indent}translate([{float_format(center_x)}, "
                              f"{float_format(center_y)}])")
            circle_indent += " "
        scad_lines.append(f"{circle_indent}circle(d={float_format(diameter)}, "
                          f"$fn={points_count});  // Circle '{name}'")


# Square:
class Square(SimplePolygon):
    """Represents a rectangular SimplePolygon."""

    # Square.__init__():
    def __init__(self, name: str, dx: float, dy: float, center: P2D = P2D(0.0, 0.0),
                 rotate: float = 0.0, corner_radius: float = 0.0, corner_count: int = 3) -> None:
        """Create a translated/rotated rectangular SimplePolygon.

        Args:
            *name* (*str*): The debugging text name to output to the
                `.scad` file.
            *dx* (*float*): The X dimension of the initial rectangle.
            *dy* (*float*): The Y dimension of the initial rectangle.
            *center* (*P2D*): The center of the rectangle.  This defaults
                to the origin (i.e. *P2D*(0.0, 0.0).)
            *rotate* (*float*): The amount to rotate the rectangle about
                its center (in radians.)  This defaults to 0.0.
            *corner_radius* (*float*): The amount to round all 4 corners by.
                This defaults to 0.0
            *corner_count* (*int*): The number points on along corner arc
                excluding the arc end-points.  This defaults to 3.

        """
        # Compute some intermediate values:
        center_x: float = center.x
        center_y: float = center.y
        half_dx: float = dx / 2.0
        half_dy: float = dy / 2.0
        half_pi: float = pi / 2.0

        # Do some argument validation:
        float_format: Callable[[float], str] = Scad.float_format
        if dx <= 0.0:
            raise ValueError(f"dx={float_format(dx)} is not positive for '{name}'")
        if dy <= 0.0:
            raise ValueError(f"dy={float_format(dy)} is not positive for '{name}'")
        if corner_radius < 0.0:
            raise ValueError(f"corner_radius={float_format(corner_radius)} "
                             f"must be non-negative for '{name}'")
        if corner_radius > 0.0 and corner_count < 0:
            raise ValueError(f"corner_count={corner_count} must be non-negative for '{name}'")
        half_dx_dy_minimum: float = min(dx, dy) / 2.0
        if corner_radius > half_dx_dy_minimum:
            raise ValueError(f"corner radius={float_format(corner_radius)} is larger than half of"
                             f" min({float_format(dx)}, {float_format(dy)})/2.0 for '{name}'")
        if half_dx == half_dy == corner_radius:
            raise ValueError(f"dx/2={float_format(half_dx)}, dy/2={float_format(half_dy)}, "
                             f"corner_radius={float_format(corner_radius)}; use Circle instead!")

        # Initialize the *SimplePolygon* parent class:
        super().__init__(name, [])

        # Fill in *square* based on *dx*, *dy*, *corner_radius* and *corner_count*
        # with *center_x* and *center_y* offseting:
        square: Square = self
        if corner_radius <= 0.0:
            # No *corner_radius*, so we cand do simple 4 point *square* (i.e. *self*):
            square.point_append(P2D(center_x + half_dx, center_y + half_dy))
            square.point_append(P2D(center_x + half_dx, center_y - half_dy))
            square.point_append(P2D(center_x - half_dx, center_y - half_dy))
            square.point_append(P2D(center_x - half_dx, center_y + half_dy))
        elif corner_radius == half_dx_dy_minimum:
            # A *square* (i.e. *self*) rectangle with fully rounded corners:
            if dx < dy:
                # The rounded ends are on the top and bottom:
                upper_center: P2D = P2D(center_x, center_y + half_dy - half_dx)
                lower_center: P2D = P2D(center_x, center_y + half_dx - half_dy)
                square.arc_append(upper_center, corner_radius, 0.0, pi, 2 * corner_count + 3)
                square.arc_append(lower_center, corner_radius, pi, 2 * pi, 2 * corner_count + 3)
            elif dy < dx:
                # The rounded ends are on the left and right:
                right_center: P2D = P2D(center_x + half_dx - half_dy, center_y)
                left_center: P2D = P2D(center_x + half_dy - half_dx, center_y)
                square.arc_append(right_center, corner_radius,
                                  -half_pi, half_pi, 2 * corner_count + 3)
                square.arc_append(left_center, corner_radius,
                                  half_pi, 3 * half_pi, 2 * corner_count + 3)
            else:  # pragma: no cover
                assert False, "This should not be possible"
        elif 0.0 < corner_radius < half_dx_dy_minimum:
            # A significantly more complicated *Rectangle* with 4 rounded corners:
            corner_center_dx: float = half_dx - corner_radius
            corner_center_dy: float = half_dy - corner_radius
            upper_right_center: P2D = P2D(center_x + corner_center_dx, center_y + corner_center_dy)
            upper_left_center: P2D = P2D(center_x - corner_center_dx, center_y + corner_center_dy)
            lower_left_center: P2D = P2D(center_x - corner_center_dx, center_y - corner_center_dy)
            lower_right_center: P2D = P2D(center_x + corner_center_dx, center_y - corner_center_dy)
            square.arc_append(upper_right_center, corner_radius, 0.0, half_pi, corner_count + 2)
            square.arc_append(upper_left_center, corner_radius, half_pi, pi, corner_count + 2)
            square.arc_append(lower_left_center, corner_radius, pi, 3 * half_pi, corner_count + 2)
            square.arc_append(lower_right_center, corner_radius,
                              3 * half_pi, 2 * pi, corner_count + 2)
        else:  # pragma: no cover
            assert False, "Problem with corner_radius; this should not happen."

        # If *rotate* is non-zero, we replace *square_points* with a verision where each
        # point is rotated by *rotate* around *center*:
        if rotate != 0.0:
            square.points_rotate(rotate, center)

        # Load values into *square* (i.e. *self*) and *lock* it:
        self.center: P2D = center
        self.corner_count: int = corner_count
        self.corner_radius: float = corner_radius
        self.dx: float = dx
        self.dy: float = dy
        self.rotate: float = rotate
        square.lock()

    # Square.__str__():
    def __str__(self) -> str:
        """Return a string representation of Circle*."""
        # Grab some values from *square* (i.e. *self*):
        square: Square = self
        center: P2D = square.center
        corner_count: int = square.corner_count
        corner_radius: float = square.corner_radius
        dx: float = square.dx
        dy: float = square.dy
        name: str = square.name
        rotate: float = square.rotate

        # Only provide *center_text*, *rotate_text*, and *corner_text* if appropriate:
        float_format: Callable[[float], str] = Scad.float_format
        center_text: str = "" if center.x == 0.0 and center.y == 0.0 else f",center={center}"
        rotate_text: str = "" if rotate == 0.0 else f",rotate={float_format(degrees(rotate))}deg"
        corner_radius_text: str = ("" if corner_radius <= 0.0
                                   else f",corner_radius={float_format(corner_radius)}")
        corner_count_text: str = ("" if corner_radius <= 0.0 or corner_count == 3
                                  else f",corner_count={corner_count}")

        # Return the formatted string reprentation:
        return (f"Square('{name}',{float_format(dx)},{float_format(dy)}"
                f"{center_text}{rotate_text}{corner_radius_text}{corner_count_text})")

    # Square.key():
    def key(self) -> Tuple[Any]:
        """Return an immutable sorting key for a Circle."""
        # Grab some values from *square* (i.e. *self*):
        square: Square = self
        center: P2D = square.center
        corner_count: int = square.corner_count
        corner_radius: float = square.corner_radius
        dx: float = square.dx
        dy: float = square.dy
        name: str = square.name
        rotate: float = square.rotate

        # (TYPE, NAME, CENTER_X, CENTER_Y, DX, DY, ROTATE, CORNER_RADIUS, CORNER_COUNT):
        key: Any[Tuple] = ("Square", name, center.x, center.y, dx, dy, degrees(rotate),
                           corner_radius, corner_count)
        return key

    # Square.scad_lines_append():
    def scad_lines_append(self, scad_lines: List[str], indent: str) -> None:
        """Append Circle to lines list.

        Args:
            *scad_lines* (*List*[*str*]): The lines list to append the
                *square* (i.e. *self*) to.
            *indent* (*str*): The indentatation prefix for each line.

        """
        # Grab some values from *circle* (i.e. *self*):
        # Grab some values from *square* (i.e. *self*):
        square: Square = self
        center: P2D = square.center
        corner_count: float = square.corner_count
        corner_radius: float = square.corner_radius
        dx: float = square.dx
        dy: float = square.dy
        name: str = square.name
        rotate: float = square.rotate

        # Output a debugging line
        float_format: Callable[[float], str] = Scad.float_format
        assert isinstance(scad_lines, list)
        scad_lines.append(f"{indent}// Square '{name}' dx={float_format(dx)} "
                          f"dy={float_format(dy)} center={center} "
                          f"corner_radius={float_format(corner_radius)} "
                          f"corner_count={corner_count}")

        if corner_radius == 0.0:
            # We can use the OpenSCAD `square` command with optional `translate` and
            # `rotate` transforms:
            center_x: float = center.x
            center_y: float = center.y
            square_indent: str = indent
            if center_x != 0.0 and center_y != 0.0:
                scad_lines.append(f"{square_indent}translate([{float_format(center.x)}, "
                                  f"{float_format(center_y)}])")
                square_indent += " "
            if rotate != 0.0:
                scad_lines.append(f"{square_indent}rotate(a = "
                                  f"[0, 0, {float_format(degrees(rotate))}])")
                square_indent += " "
            scad_lines.append(f"{square_indent}square([{float_format(dx)}, {float_format(dy)}], "
                              "center = true);")
        else:
            # Rounded corners need to be done with an OpenSCAD `polygon` command:
            square.polygon_scad_lines_append([square], scad_lines, indent)


# Scad3D:
class Scad3D(Scad):
    """Represents 3-dimensional Scad objects."""

    def __init__(self, name: str) -> None:
        """Set the name of the 3-dimensional SCAD object."""
        super().__init__(name)


# LinearExtrude():
class LinearExtrude(Scad3D):
    """Represents an OpenScad `linear_extrude` command."""

    def __init__(self, name: str, scad2d: Scad2D, height: float, center: bool = False,
                 twist: float = 0.0, convexity: int = -1, slices: int = -1,
                 initial_scale: float = 1.0, final_scale: float = 1.0) -> None:
        """Initialize a `linear_extrude` command.

        Args:
            *name* (*str*): A name that will be output to the
                `.scad` file.
            *scad2d*: (*Scad2D*): A 2-dimensional *Scad* object to
                perform the linear extrusion on.
            *height* (*float*): The height of the extrusion.
            *center* (*bool*): If *True*, the extrusion is from
                -*height*/2 to *height*/2 in the Z direction;
                otherwise, it is from 0 to *height* in the Z direction.
            *convexity* (*int*): Specifies the complexity level to
                support for preview rendering.  Higher numbers support
                more complex objects.
            *twist* (*float*): Specifies the amount of twist around the
                Z axis in radians.
            *slices*: (*int*): Specifies
            *initial_scale* (*float*): Specifies the initial scale
                of the linear extrusion.
            *final_scale* (*float*): Specifies the final scale of
                the linear extrusion.

        """
        # Initialize the *Scad* base-class:
        super().__init__(name)

        # Do some argument range validation:
        assert final_scale > 0.0, f"final_scale={final_scale}; it needs to be positive"
        assert height > 0.0, f"height={height}; it needs to be positive"
        assert initial_scale > 0.0, f"initial_scale={initial_scale}; it needs to be positive"

        # Initialize the *scad_linear_extrude* (i.e. *self*):
        self.center: bool = center
        self.convexity: int = 10 if convexity <= 0 else convexity
        self.final_scale: float = final_scale
        self.height: float = height
        self.initial_scale: float = initial_scale
        self.scad2d: Scad2D = scad2d
        self.slices: int = slices
        self.twist: float = twist

    # LinearExtrude.scad_lines_append():
    def scad_lines_append(self, scad_lines: List[str], indent: str) -> None:
        """Append ScadLinearExtrude to list of lines.

        Args:
            *scad_lines* (*List*[*str*]): The lines list to append the
                *scad_polygon* (i.e. *self*) to.
            *indent* (*str*): The indentatation prefix for each line.

        """
        # Grab some values from *scad_linear_extrude* (i.e. *self*):
        linear_extrude: LinearExtrude = self
        center: bool = linear_extrude.center
        convexity: int = linear_extrude.convexity
        final_scale: float = linear_extrude.final_scale
        initial_scale: float = linear_extrude.initial_scale
        height: float = linear_extrude.height
        name: str = linear_extrude.name
        scad2d: Scad2D = linear_extrude.scad2d
        slices: int = linear_extrude.slices
        twist: float = linear_extrude.twist

        # Compute *scale_text* and *slices_text*:
        scale_text: str = ""
        float_format: Callable[[float], str] = Scad.float_format
        if initial_scale != 1.0:
            scale_text = f", scale=[{float_format(initial_scale)}, {float_format(final_scale)}]"
        elif final_scale != 1.0:
            scale_text = f", scale={float_format(final_scale)}"
        slices_text: str = f", slices={slices}" if slices > 0 else ""

        # Perform the the `linear_extrude` command append to *scad_lines*:
        scad_lines.append(f"{indent}// Begin LinearExtrude '{name}'")
        scad_lines.append(f"{indent}linear_extrude("
                          f"height={height}"
                          f", center={str(center).lower()}"
                          f", convexity={convexity}"
                          f", twist={degrees(twist)}"
                          f"{slices_text}{scale_text})")

        # Append the *scad2d* object next:
        scad2d.scad_lines_append(scad_lines, indent + " ")

        # Outut an end comment:
        scad_lines.append(f"{indent}// End LinearExtrude '{name}'")


# Polygon:
class Polygon(Scad2D):
    """Represents an OpenScad `polygon` command."""

    # Polygon.__init__():
    def __init__(self, name: str, simple_polygons: List[SimplePolygon],
                 convexity: int = -1, lock=True) -> None:
        """Initialize an OpenSCAD polygon command.

        Initialze a *Polygon* object to initially contain a list of
        *simple_polygons.*  If *locked* is *True*, no additional
        *SimplePolygon*'s can be append to *polygon* (i.e. *self*);
        otherwise both the *Polygon*.*append*() and the
        *Polygon*.*extend*() methods can be used to append additional
        *SimplePolygon*'s.  The *Polygon*.*lock() forces *polygon*
        to be locked and it can not be unlocked afterwards.


        Args:
            *name*: (*str*): The name of OpenSCAD polygon command.
            *simple_polygons* (*List*[*SimplePolygon*]): A list of
                *SimplePolygon*'s to install into *polygon*
                (i.e. *self*).  Each of these *SimplePolygon*"s must
                be locked.
            *convexity* (*int*): A number to estimate the complexit
                of the polygon.  Higher numbers are needed for
                accurate complex polygon rendering.  If no value is
                provided, a resonable default is provided.
            *lock* (*bool*): If *True* the initialized *polygon*
                object (i.e. *self*) is locked from having additional
                *SimplePolygon*'s appended to it; other no additional
                *SimplePolygon*'s can be appended.

        Raises:
            *ValueError*(*str*): if any of the *SimplePolygon*'s in
                *simple_polygons* are not locked .

        """
        # Valid that all of the *simple_polygons* are locked:
        simple_polygon_index: int
        simple_polygon: SimplePolygon
        for simple_polygon_index, simple_polygon in enumerate(simple_polygons):
            if not simple_polygon.is_locked():
                simple_polygon_name: str = simple_polygon.name
                raise ValueError(f"SimplePolygon ('{simple_polygon_name}') "
                                 f"at index {simple_polygon_index} is not locked.")

        # Intilize the base class and stuff values into *scad_polygon* (i.e. *self*):
        super().__init__(name)
        self.locked: bool = lock
        self.convexity: int = convexity
        self.simple_polygons: List[SimplePolygon] = simple_polygons[:]

    # Polygon.__getitem__():
    def __getitem__(self, index: int) -> SimplePolygon:
        """Return the selected Polygon.

        Args:
            *index* (*int*): The index into the *polygon*
                (i.e. *self*) *Polygon*'s list to fetch.

        Returns:
            (*SimplePolygon*) Returns the selected *SimplePolygon*:

        """
        # Grab some values from *polygon* (i.e. *self*):
        polygon: Polygon = self
        simple_polygons: List[SimplePolygon] = polygon.simple_polygons
        simple_polygons_size: int = len(simple_polygons)
        if index < 0 or index >= simple_polygons_size:
            raise IndexError(f"index={index} and it is not in range 0:{simple_polygons_size-1}")
        simple_polygon: SimplePolygon = simple_polygons[index]
        return simple_polygon

    # Polygon.__len__()
    def __len__(self):
        """Return the number of SimplePolygon's in the Polygon.

        Returns:
            (*int*) Returns the number of *SimplePolygon*'s in *polygon*
                (i.e. *self*.)

        """
        # Grab the *polygons* from *scad_polygon* (i.e. *self*):
        polygon: polygon = self
        simple_polygons: List[SimplePolygon] = polygon.simple_polygons
        simple_polygons_size: int = len(simple_polygons)
        return simple_polygons_size

    # Polygon.__str__():
    def __str__(self) -> str:
        """Return string for *Polygon."""
        # Grab *name* from *polygon* (i.e. *self*) and return formatted string:
        polygon: Polygon = self
        name: str = polygon.name
        simple_polygons: List[SimplePolygon] = polygon.simple_polygons
        simple_polygons_size: int = len(simple_polygons)
        convexity: int = polygon.convexity
        return (f"Polygon('{name}',"
                f"len(simple_polygons)={simple_polygons_size},"
                f"convexity={convexity})")

    # Polygon.append():
    def append(self, simple_polygon: SimplePolygon) -> None:
        """Append a SimplePolygon to the Polygon.

        Args:
            *simple_polygon*: (*SimplePolygon*): The *SimplePolygon*
                to append to *polygon* (i.e. *self*.)

        """
        # Grab some values from *polygon* (i.e. *self*):
        polygon: Polygon = self
        simple_polygons: List[SimplePolygon] = polygon.simple_polygons
        simple_polygons.append(simple_polygon)

    # Polygon.extend():
    def extend(self, additional_simple_polygons: List[SimplePolygon]) -> None:
        """Append a list of SimplePolygon's to the Polygon.

        Args:
            *additional_simple_polygons*: (*List*[*SimplePolygon*]):
                The list of *SimplePolygon*'s  to append to
                *scad_polygon* (i.e. *self*.)

        """
        # Grab some values from *polygon* (i.e. *self*):
        polygon: Polygon = self
        simple_polygons: List[SimplePolygon] = polygon.simple_polygons
        simple_polygons.extend(additional_simple_polygons)

    # Polygon.scad_lines_append():
    def scad_lines_append(self, scad_lines: List[str], indent: str) -> None:
        """Append Polygon commands to a lines list.

        Args:
            *scad_lines* (*List*[*str*]): The lines list to append the
                *scad_polygon* (i.e. *self*) to.
            *indent* (*str*): The indentatation prefix for each line.

        """
        polygon: Polygon = self
        simple_polygons: List[SimplePolygon] = polygon.simple_polygons
        polygon.polygon_scad_lines_append(simple_polygons, scad_lines, indent)


# Union:
class Union(Scad):
    """Represents a boolean union of SCAD objects."""

    # Union.__init__():
    def __init__(self, name: str, scads: List[Scad]) -> None:
        """Initialize a Union object.

        Args:
            *name* (*str*): The name that is output to the `.scad`
                file.
            *scads* (*List*[*Scad*]): A list of *Scad* objects
                to be unioned together.  All of the *Scad* objects
                must be either *Scad2D* or *Scad3D*; there  is no
                mixing allowed between the two.

        Raises:
            *ValueError*(*str*): Exception that is raised when there are
                mixed *Scad2D* and *Scad3D* object in *scads*:

        """
        # Initialize the base class:
        super().__init__(name)

        # Validate that there are no mixed *Scad2D* and *Scad3D objects in *scads*:
        if scads:
            scads0: Scad = scads[0]
            scads0_class_name = scads0.__class__.__name__
            scad: Scad
            scad_index: int
            for scad_index, scad in enumerate(scads):
                scad_class_name: str = scad.__class__.__name__
                if scads0_class_name != scad_class_name:
                    raise ValueError(f"Index 0 of Union is class '{scads0_class_name},' "
                                     f"but index {scad_index} is class '{scad_class_name}'")

        # If we get there far, we can stuf *scads* into *union* (i.e. *self*):
        # union: Union = self
        self.scads: List[Scad] = scads[:]

    # Union.scad_lines_append():
    def scad_lines_append(self, scad_lines: List[str], indent: str) -> None:
        """Append Union to list of lines.

        Args:
            *scad_lines* (*List*[*str*]): The lines list to append the
                *scad_polygon* (i.e. *self*) to.
            *indent* (*str*): The indentatation prefix for each line.

        """
        # Grab some values from *scad_3d_union* (i.e: *self*):
        union: Union = self
        name: str = union.name
        scads: List[Scad] = union.scads

        # Append the lines to *scad_lines*:
        scad_lines.append(f"{indent}// Union '{name}'")
        scad_lines.append(f"{indent}union() {{")
        next_indent: str = indent + " "
        scad: Scad
        for scad in scads:
            scad.scad_lines_append(scad_lines, next_indent)
        scad_lines.append(f"{indent}// End Union '{name}'")
        scad_lines.append(f"{indent}}}")
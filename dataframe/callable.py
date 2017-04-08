# dataframe: a data-frame implementation using method piping
#
# Copyright (C) 2016 Simon Dirmeier
#
# This file is part of dataframe.
#
# dataframe is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# dataframe is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with dataframe. If not, see <http://www.gnu.org/licenses/>.
#
#
# @author = 'Simon Dirmeier'
# @email = 'mail@simon-dirmeier.net'


class Callable:
    """
    Super-class for all classes that should be callable.
     
    E.g.: whenever you want to use ``modify`` or ``aggregate`` you need to
    write a class that extends ``Callable`` and overwrite ``__call__``.
    
    ``__call__`` has to return a scalar or list, depending if you want to
    aggregate columns or modify. So a class that modifies a column returns
    list, while a class that aggregates returns a scalar.
    """

    def __call__(self, *args):
        """
        Call method. Is used when object is called like this: object()

        :param args: tuple of columns
        :type args: tuple
        :return: returns a list/scalar
        :rtype: list(any)/scalar
        """
        pass

#!/usr/bin/env python3
from itertools import permutations

class Tensor(object):

    """Print tensor in matrix form."""

    def __init__(self, order=1, size=1, fill=None):
        """Initialize a tensor of 'order'
        dimensions with 'size' elements in
        each dimension.

        :order: number of dimensions of the tensor
        :size: number of elements in each dimension

        """
        self._order = order
        self._size  = size
        self._fill  = fill
        self._numElems = self._size**self._order
        self._index = []
        if self._fill == 'index':
            self._data = self.fill_index()
        else:
            self._data  = [self._fill for i in range(self._numElems)]
    
    def get(self, index):
        try:
            assert(len(index) == self._order), "Invalid selection!"
            elem = self._baseToNumber(self._size, index)
            assert(elem >= 0 and
                   elem <= self._numElems), "Invalid selection!"
            return(self._data[elem])
        except:
            raise(BaseException)
    
    def set(self, index, value):
        try:
            assert(len(index) == self._order), "Invalid selection!"
            elem = self._baseToNumber(self._size, index)
            assert(elem >= 0 and
                   elem <= self._numElems), "Invalid selection!"
            self._data[elem] = value
        except:
            raise(BaseException)
    
    def fill_index(self):
        if not self._index:
            for i in range(self._numElems):
                self._index.append(self._numberToBase(self._size, str(i), just=self._order))
        return(self._index)
    
    def data(self):
        return(self._data)
    
    def print_data(self):
        """Pretty print the tensor data in matrix form.
        """
        pass
    
    def _numberToBase(self, bnum, nstring, just=0):
        n = int(nstring)
        if n == 0:
            return('0'.rjust(just, '0'))
        digits = []
        while n:
            digits.append(int(n % bnum))
            n //= bnum
        to_return = (''.join([str(i) for i in digits[::-1]]))
        return(to_return.rjust(just, '0'))
    
    def _baseToNumber(self, bnum, nstring):
        n = [int(i) for i in list(nstring.lstrip('0'))]
        p = [bnum**int(i) for i in range(len(n))][::-1]
        return(sum([k*v for k,v in zip(p, n)]))
    
    def sym_perms_4i(self, ints, notation='phys', return_type=str): 
        '''
        TODO: write docstrings
        '''
        
        if notation   == 'phys':
            bk_off, el_off = 2, 1
        elif notation == 'chem':
            bk_off, el_off = 1, 2

        bra = 0
        ket = bra+bk_off

        e1_bra = ints[bra]
        e1_ket = ints[ket]
        # e2_bra = ints[bra+el_off]
        # e2_ket = ints[ket+el_off]

        all_perms = permutations(ints) 
        s = [] 
        to_print = []
        for p in all_perms: 
            if (e1_bra, e1_ket) in ((p[0], p[0+bk_off]),
                                    (p[0+bk_off], p[0]),
                                    (p[el_off], p[el_off+bk_off]),
                                    (p[el_off+bk_off], p[el_off])):
                s.append(tuple(return_type(xx) for xx in p))
        s = list(set(s))
        s.sort()
        return(s)
    
    def label_elem_4i(self, notation='phys'):
        '''
        Get a tensor with unique elements labelled numerically.
        
        If two different positions have the
        same label, they have same elements due to
        permutatioinal symmetry
        '''
        pass

class FourIndexTensor(Tensor):
    pass

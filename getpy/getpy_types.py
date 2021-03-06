import numpy as np

import _getpy as _gp

dict_types = {
    (np.dtype('u4'), np.dtype('u1')) : _gp.Dict_u4_u1,
    (np.dtype('u4'), np.dtype('u2')) : _gp.Dict_u4_u2,
    (np.dtype('u4'), np.dtype('u4')) : _gp.Dict_u4_u4,
    (np.dtype('u4'), np.dtype('u8')) : _gp.Dict_u4_u8,
    (np.dtype('u4'), np.dtype('i1')) : _gp.Dict_u4_i1,
    (np.dtype('u4'), np.dtype('i2')) : _gp.Dict_u4_i2,
    (np.dtype('u4'), np.dtype('i4')) : _gp.Dict_u4_i4,
    (np.dtype('u4'), np.dtype('i8')) : _gp.Dict_u4_i8,
    (np.dtype('u4'), np.dtype('f4')) : _gp.Dict_u4_f4,
    (np.dtype('u4'), np.dtype('f8')) : _gp.Dict_u4_f8,
    (np.dtype('u4'), np.dtype('S8')) : _gp.Dict_u4_S8,
    (np.dtype('u4'), np.dtype('S16')) : _gp.Dict_u4_S16,
    (np.dtype('u8'), np.dtype('u1')) : _gp.Dict_u8_u1,
    (np.dtype('u8'), np.dtype('u2')) : _gp.Dict_u8_u2,
    (np.dtype('u8'), np.dtype('u4')) : _gp.Dict_u8_u4,
    (np.dtype('u8'), np.dtype('u8')) : _gp.Dict_u8_u8,
    (np.dtype('u8'), np.dtype('i1')) : _gp.Dict_u8_i1,
    (np.dtype('u8'), np.dtype('i2')) : _gp.Dict_u8_i2,
    (np.dtype('u8'), np.dtype('i4')) : _gp.Dict_u8_i4,
    (np.dtype('u8'), np.dtype('i8')) : _gp.Dict_u8_i8,
    (np.dtype('u8'), np.dtype('f4')) : _gp.Dict_u8_f4,
    (np.dtype('u8'), np.dtype('f8')) : _gp.Dict_u8_f8,
    (np.dtype('u8'), np.dtype('S8')) : _gp.Dict_u8_S8,
    (np.dtype('u8'), np.dtype('S16')) : _gp.Dict_u8_S16,
    (np.dtype('i4'), np.dtype('u1')) : _gp.Dict_i4_u1,
    (np.dtype('i4'), np.dtype('u2')) : _gp.Dict_i4_u2,
    (np.dtype('i4'), np.dtype('u4')) : _gp.Dict_i4_u4,
    (np.dtype('i4'), np.dtype('u8')) : _gp.Dict_i4_u8,
    (np.dtype('i4'), np.dtype('i1')) : _gp.Dict_i4_i1,
    (np.dtype('i4'), np.dtype('i2')) : _gp.Dict_i4_i2,
    (np.dtype('i4'), np.dtype('i4')) : _gp.Dict_i4_i4,
    (np.dtype('i4'), np.dtype('i8')) : _gp.Dict_i4_i8,
    (np.dtype('i4'), np.dtype('f4')) : _gp.Dict_i4_f4,
    (np.dtype('i4'), np.dtype('f8')) : _gp.Dict_i4_f8,
    (np.dtype('i4'), np.dtype('S8')) : _gp.Dict_i4_S8,
    (np.dtype('i4'), np.dtype('S16')) : _gp.Dict_i4_S16,
    (np.dtype('i8'), np.dtype('u1')) : _gp.Dict_i8_u1,
    (np.dtype('i8'), np.dtype('u2')) : _gp.Dict_i8_u2,
    (np.dtype('i8'), np.dtype('u4')) : _gp.Dict_i8_u4,
    (np.dtype('i8'), np.dtype('u8')) : _gp.Dict_i8_u8,
    (np.dtype('i8'), np.dtype('i1')) : _gp.Dict_i8_i1,
    (np.dtype('i8'), np.dtype('i2')) : _gp.Dict_i8_i2,
    (np.dtype('i8'), np.dtype('i4')) : _gp.Dict_i8_i4,
    (np.dtype('i8'), np.dtype('i8')) : _gp.Dict_i8_i8,
    (np.dtype('i8'), np.dtype('f4')) : _gp.Dict_i8_f4,
    (np.dtype('i8'), np.dtype('f8')) : _gp.Dict_i8_f8,
    (np.dtype('i8'), np.dtype('S8')) : _gp.Dict_i8_S8,
    (np.dtype('i8'), np.dtype('S16')) : _gp.Dict_i8_S16,
    (np.dtype('S8'), np.dtype('u1')) : _gp.Dict_S8_u1,
    (np.dtype('S8'), np.dtype('u2')) : _gp.Dict_S8_u2,
    (np.dtype('S8'), np.dtype('u4')) : _gp.Dict_S8_u4,
    (np.dtype('S8'), np.dtype('u8')) : _gp.Dict_S8_u8,
    (np.dtype('S8'), np.dtype('i1')) : _gp.Dict_S8_i1,
    (np.dtype('S8'), np.dtype('i2')) : _gp.Dict_S8_i2,
    (np.dtype('S8'), np.dtype('i4')) : _gp.Dict_S8_i4,
    (np.dtype('S8'), np.dtype('i8')) : _gp.Dict_S8_i8,
    (np.dtype('S8'), np.dtype('f4')) : _gp.Dict_S8_f4,
    (np.dtype('S8'), np.dtype('f8')) : _gp.Dict_S8_f8,
    (np.dtype('S8'), np.dtype('S8')) : _gp.Dict_S8_S8,
    (np.dtype('S8'), np.dtype('S16')) : _gp.Dict_S8_S16,
    (np.dtype('S16'), np.dtype('u1')) : _gp.Dict_S16_u1,
    (np.dtype('S16'), np.dtype('u2')) : _gp.Dict_S16_u2,
    (np.dtype('S16'), np.dtype('u4')) : _gp.Dict_S16_u4,
    (np.dtype('S16'), np.dtype('u8')) : _gp.Dict_S16_u8,
    (np.dtype('S16'), np.dtype('i1')) : _gp.Dict_S16_i1,
    (np.dtype('S16'), np.dtype('i2')) : _gp.Dict_S16_i2,
    (np.dtype('S16'), np.dtype('i4')) : _gp.Dict_S16_i4,
    (np.dtype('S16'), np.dtype('i8')) : _gp.Dict_S16_i8,
    (np.dtype('S16'), np.dtype('f4')) : _gp.Dict_S16_f4,
    (np.dtype('S16'), np.dtype('f8')) : _gp.Dict_S16_f8,
    (np.dtype('S16'), np.dtype('S8')) : _gp.Dict_S16_S8,
    (np.dtype('S16'), np.dtype('S16')) : _gp.Dict_S16_S16,
}

set_types = {
    np.dtype('u4') : _gp.Set_u4,
    np.dtype('u8') : _gp.Set_u8,
    np.dtype('i4') : _gp.Set_i4,
    np.dtype('i8') : _gp.Set_i8,
    np.dtype('S8') : _gp.Set_S8,
    np.dtype('S16') : _gp.Set_S16,
}

multidict_types = {
    (np.dtype('u4'), np.dtype('u4')) : _gp.MultiDict_u4_u4,
    (np.dtype('u4'), np.dtype('u8')) : _gp.MultiDict_u4_u8,
    (np.dtype('u4'), np.dtype('i4')) : _gp.MultiDict_u4_i4,
    (np.dtype('u4'), np.dtype('i8')) : _gp.MultiDict_u4_i8,
    (np.dtype('u4'), np.dtype('S8')) : _gp.MultiDict_u4_S8,
    (np.dtype('u4'), np.dtype('S16')) : _gp.MultiDict_u4_S16,
    (np.dtype('u8'), np.dtype('u4')) : _gp.MultiDict_u8_u4,
    (np.dtype('u8'), np.dtype('u8')) : _gp.MultiDict_u8_u8,
    (np.dtype('u8'), np.dtype('i4')) : _gp.MultiDict_u8_i4,
    (np.dtype('u8'), np.dtype('i8')) : _gp.MultiDict_u8_i8,
    (np.dtype('u8'), np.dtype('S8')) : _gp.MultiDict_u8_S8,
    (np.dtype('u8'), np.dtype('S16')) : _gp.MultiDict_u8_S16,
    (np.dtype('i4'), np.dtype('u4')) : _gp.MultiDict_i4_u4,
    (np.dtype('i4'), np.dtype('u8')) : _gp.MultiDict_i4_u8,
    (np.dtype('i4'), np.dtype('i4')) : _gp.MultiDict_i4_i4,
    (np.dtype('i4'), np.dtype('i8')) : _gp.MultiDict_i4_i8,
    (np.dtype('i4'), np.dtype('S8')) : _gp.MultiDict_i4_S8,
    (np.dtype('i4'), np.dtype('S16')) : _gp.MultiDict_i4_S16,
    (np.dtype('i8'), np.dtype('u4')) : _gp.MultiDict_i8_u4,
    (np.dtype('i8'), np.dtype('u8')) : _gp.MultiDict_i8_u8,
    (np.dtype('i8'), np.dtype('i4')) : _gp.MultiDict_i8_i4,
    (np.dtype('i8'), np.dtype('i8')) : _gp.MultiDict_i8_i8,
    (np.dtype('i8'), np.dtype('S8')) : _gp.MultiDict_i8_S8,
    (np.dtype('i8'), np.dtype('S16')) : _gp.MultiDict_i8_S16,
    (np.dtype('S8'), np.dtype('u4')) : _gp.MultiDict_S8_u4,
    (np.dtype('S8'), np.dtype('u8')) : _gp.MultiDict_S8_u8,
    (np.dtype('S8'), np.dtype('i4')) : _gp.MultiDict_S8_i4,
    (np.dtype('S8'), np.dtype('i8')) : _gp.MultiDict_S8_i8,
    (np.dtype('S8'), np.dtype('S8')) : _gp.MultiDict_S8_S8,
    (np.dtype('S8'), np.dtype('S16')) : _gp.MultiDict_S8_S16,
    (np.dtype('S16'), np.dtype('u4')) : _gp.MultiDict_S16_u4,
    (np.dtype('S16'), np.dtype('u8')) : _gp.MultiDict_S16_u8,
    (np.dtype('S16'), np.dtype('i4')) : _gp.MultiDict_S16_i4,
    (np.dtype('S16'), np.dtype('i8')) : _gp.MultiDict_S16_i8,
    (np.dtype('S16'), np.dtype('S8')) : _gp.MultiDict_S16_S8,
    (np.dtype('S16'), np.dtype('S16')) : _gp.MultiDict_S16_S16,
}

class CubesCodeGenerator:

    def __init__(self) -> None:
        self.membercount = 0

    def generate(self, name, xoffset = 0.0, yoffset = 0.0, zoffset = 0.0, size = 1):

        v1base = (-1.000000 * size, -1.000000 * size,  1.000000 * size)
        v2base = (-1.000000 * size,  1.000000 * size,  1.000000 * size)
        v3base = (-1.000000 * size, -1.000000 * size, -1.000000 * size)
        v4base = (-1.000000 * size,  1.000000 * size, -1.000000 * size)
        v5base = ( 1.000000 * size, -1.000000 * size,  1.000000 * size)
        v6base = ( 1.000000 * size,  1.000000 * size,  1.000000 * size)
        v7base = ( 1.000000 * size, -1.000000 * size, -1.000000 * size)
        v8base = ( 1.000000 * size,  1.000000 * size, -1.000000 * size)

        v1 = (v1base[0] + xoffset, v1base[1] + yoffset, v1base[2] + zoffset)
        v2 = (v2base[0] + xoffset, v2base[1] + yoffset, v2base[2] + zoffset)
        v3 = (v3base[0] + xoffset, v3base[1] + yoffset, v3base[2] + zoffset)
        v4 = (v4base[0] + xoffset, v4base[1] + yoffset, v4base[2] + zoffset)
        v5 = (v5base[0] + xoffset, v5base[1] + yoffset, v5base[2] + zoffset)
        v6 = (v6base[0] + xoffset, v6base[1] + yoffset, v6base[2] + zoffset)
        v7 = (v7base[0] + xoffset, v7base[1] + yoffset, v7base[2] + zoffset)
        v8 = (v8base[0] + xoffset, v8base[1] + yoffset, v8base[2] + zoffset)
        
        base_string = '''
o {0}
v {1} {2} {3}
v {4} {5} {6}
v {7} {8} {9}
v {10} {11} {12}
v {13} {14} {15}
v {16} {17} {18}
v {19} {20} {21}
v {22} {23} {24}

vn -1.0000 -0.0000 -0.0000
vn -0.0000 -0.0000 -1.0000
vn 1.0000 -0.0000 -0.0000
vn -0.0000 -0.0000 1.0000
vn -0.0000 -1.0000 -0.0000
vn -0.0000 1.0000 -0.0000

s 0
'''
        part_one_string = base_string.format(name, 
            v1[0], v1[1], v1[2], 
            v2[0], v2[1], v2[2],
            v3[0], v3[1], v3[2],
            v4[0], v4[1], v4[2],
            v5[0], v5[1], v5[2],
            v6[0], v6[1], v6[2],
            v7[0], v7[1], v7[2],
            v8[0], v8[1], v8[2]
        )

        final_string = part_one_string + self.__generatef()

        self.membercount += 1

        return final_string

    def __generatef(self):

        v1number = 1 + 8 * self.membercount
        v2number = 2 + 8 * self.membercount
        v3number = 3 + 8 * self.membercount
        v4number = 4 + 8 * self.membercount
        v5number = 5 + 8 * self.membercount
        v6number = 6 + 8 * self.membercount
        v7number = 7 + 8 * self.membercount
        v8number = 8 + 8 * self.membercount

        base_string_2 = '''f {0}//1 {1}//1 {3}//1 {2}//1
f {2}//2 {3}//2 {7}//2 {6}//2
f {6}//3 {7}//3 {5}//3 {4}//3
f {4}//4 {5}//4 {1}//4 {0}//4
f {2}//5 {6}//5 {4}//5 {0}//5
f {7}//6 {3}//6 {1}//6 {5}//6
'''

        return base_string_2.format(v1number, v2number, v3number, v4number, v5number, v6number, v7number, v8number)
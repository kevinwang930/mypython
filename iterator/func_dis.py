import dis

def test(up_to):
        index = 0
        while index < up_to:
            jump = yield index
            if jump is None:
                jump = 1
            index += jump

dis.dis(test)


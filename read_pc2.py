from struct import unpack


def read_pc2(filepath):

    with open(filepath, 'rb') as f:

        # Read info from the file header
        headerFormat = '<12ciiffi'
        header = unpack(headerFormat, f.read(32))
        print(header)

        # fileVersion = header[12]
        numPoints = header[13]
        startFrame = int(header[14])
        sampleRate = header[15]
        numSamples = header[16]

        print('\tnumPoints:%d startFrame:%d sampleRate:%d numSamples:%d'
              % (numPoints, startFrame, sampleRate, numSamples))

        vertexFormat = '<3f'
        vertices = []
        # vertex = unpack(vertexFormat, f.read(12))
        # print(vertex)
        for i in range(numSamples*numPoints):
            vertex = unpack(vertexFormat, f.read(12))
            vertices.append(vertex)
            print(vertex)
        print(len(vertices))
    return vertices


# read_pc2('animation_data_2.pc2')
#
read_pc2('test_gaussian_pc2.pc2')
import hashlib
import pickle


def ToBytes(obj):
    return pickle.dumps(obj)


# def FromBytes(obj):
#     print(pickle.dumps(obj).decode())


def Hash(target):
    return hashlib.sha256(ToBytes(target)).hexdigest()


if __name__ == "__main__":
    print(Hash("hi"))

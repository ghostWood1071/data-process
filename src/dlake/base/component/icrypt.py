from dlake.base.type.crypt import CryptType
from dlake.base.type.key import KeyType



class ICrypt:
    def __init__(self):
        pass

    def import_pkey(self, key: str, key_type: KeyType = None):
        pass

    def export_pkey(self):
        pass

    def encrypt(self):
        pass

    def decrypt(self):
        pass

    def encrypt_file(self, input_path: str, output_path: str = None):
        pass

    def encrypt_folder(self, input_path: str, output_path: str = None):
        pass

    def decrypt_file(self, input_path: str, output_path: str = None):
        pass

    def decrypt_folder(self, input_path: str, output_path: str = None):
        pass

    @staticmethod
    def init(crypt_type: CryptType):
        match crypt_type:
            case CryptType.GPG:
                from dlake.base.component.crypt.pgp import PGPCrypt
                return PGPCrypt()
            case _:
                return ICrypt()

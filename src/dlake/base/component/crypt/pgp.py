import re
import gnupg

from dlake.base.type.crypt import CryptType
from dlake.base.type.key import KeyType
from dlake.base.util.logger import Logger
from dlake.core.component import ICrypt

LOGGER = Logger.get_logger("PGPCrypt")


class PGPCrypt(ICrypt):
    def __init__(self):
        super().__init__(type=CryptType.GPG)
        self.gpg = gnupg.GPG(gnupghome='C:\\Users\\hvsinh\\tmp')
        self.import_result = None

    def import_pkey(self, key: str, type: KeyType = None):
        self.import_result = self.gpg.import_keys(key)

    def export_pkey(self):
        super().export_pkey()

    def encrypt(self):
        super().encrypt()

    def decrypt(self):
        super().decrypt()

    def encrypt_file(self, file_path: str):
        output_path = file_path + ".pgp"
        LOGGER.debug("[encrypt_file] Encrypting file %s to file %s", file_path, output_path)
        if self.import_result is None:
            raise Exception('Import result is None')
        with open(file_path, 'rb') as f:
            encrypted_data = self.gpg.encrypt_file(f, armor=False, always_trust=True,
                                                   recipients=self.import_result.fingerprint, output=output_path)
            LOGGER.debug("[encrypt_file] encrypted_data", encrypted_data)
        return output_path

    def decrypt_file(self, file_path: str, passphrase: str = None):
        output_path = re.sub(".pgp$", "", file_path)
        LOGGER.debug("[decrypt_file] Decrypting file %s to file %s", file_path, output_path)
        if self.import_result is None:
            raise Exception('Import result is None')
        with open(file_path, 'rb') as f:
            decrypted_data = self.gpg.decrypt_file(f, passphrase=passphrase, output=output_path)
            LOGGER.debug("[decrypt_file] decrypted_data", decrypted_data)
        return output_path


if __name__ == '__main__':
    input_file = '..\\exams\\answers.sql'
    pub_path = 'C:\\Users\\hvsinh\\Downloads\\0xACA55A48-pub.asc'
    pri_path = 'C:\\Users\\hvsinh\\Downloads\\0xACA55A48-sec.asc'
    encrypt = PGPCrypt()
    private_key = None
    public_key = None
    with open(pri_path, 'r') as f:
        private_key = f.read()

    with open(pub_path, 'r') as f:
        public_key = f.read()

    print('private_key ', private_key)
    print('public_key ', public_key)

    encrypt.import_pkey(key=public_key)
    print(encrypt.encrypt_file(file_path=input_file))

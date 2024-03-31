import datetime

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend


def generatec_ca():
    # Generate CA key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )

    # Write our key to disk for safe keeping
    with open("cert/key.pem", "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(b"hello"),
        ))
    # Generate CA certificate

    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, u"CN"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"guangdong"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, u"dongguan"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"My Company"),
        x509.NameAttribute(NameOID.COMMON_NAME, u"CA Certificate"),
    ])

    cert = x509.CertificateBuilder().subject_name(subject).issuer_name(issuer). \
        public_key(private_key.public_key()).serial_number(x509.random_serial_number()). \
        not_valid_before(datetime.datetime.utcnow()).not_valid_after(
        datetime.datetime.utcnow() + datetime.timedelta(days=365)). \
        add_extension(x509.BasicConstraints(ca=True, path_length=None), critical=True). \
        sign(private_key, hashes.SHA256(), default_backend())

    with open("cert/ca.pem", "wb") as f:
        f.write(cert.public_bytes(serialization.Encoding.PEM))


def server_csr():
    key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    with open("cert/server/key.pem", "wb") as f:
        f.write(key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(b"hello"),
        ))
    csr = x509.CertificateSigningRequestBuilder().subject_name(x509.Name([
        # Provide various details about who we are.
        x509.NameAttribute(NameOID.COUNTRY_NAME, u"CN"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"guangdong"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, u"dongguan"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"My Company"),
        x509.NameAttribute(NameOID.COMMON_NAME, u"localhost"),
    ])).sign(key, hashes.SHA256())
    # Write our CSR out to disk.
    with open("cert/server/csr.pem", "wb") as f:
        f.write(csr.public_bytes(serialization.Encoding.PEM))


def server_cert():
    with open('cert/ca.pem', 'rb') as ca_file:
        ca_cert = x509.load_pem_x509_certificate(ca_file.read(), default_backend())

    # Load the CSR
    with open('cert/server/csr.pem', 'rb') as csr_file:
        csr = x509.load_pem_x509_csr(csr_file.read(), default_backend())

    with open('cert/key.pem', 'rb') as key_file:
        ca_key = serialization.load_pem_private_key(
            key_file.read(),
            password=b'hello',
            backend=default_backend()
        )

    # Generate the certificate
    cert = (
        x509.CertificateBuilder()
        .subject_name(csr.subject)
        .issuer_name(ca_cert.subject)
        .public_key(csr.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(ca_cert.not_valid_before)
        .not_valid_after(ca_cert.not_valid_after)
        .sign(ca_key, ca_cert.signature_hash_algorithm)
    )

    # Save the certificate to a file
    with open('cert/server/cert.pem', 'wb') as cert_file:
        cert_file.write(cert.public_bytes(serialization.Encoding.PEM))

def client_csr():
    key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    with open("cert/client/key.pem", "wb") as f:
        f.write(key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(b"hello"),
        ))
    csr = x509.CertificateSigningRequestBuilder().subject_name(x509.Name([
        # Provide various details about who we are.
        x509.NameAttribute(NameOID.COUNTRY_NAME, u"CN"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"guangdong"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, u"dongguan"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"My Company"),
        x509.NameAttribute(NameOID.COMMON_NAME, u"client"),
    ])).sign(key, hashes.SHA256())
    # Write our CSR out to disk.
    with open("cert/client/csr.pem", "wb") as f:
        f.write(csr.public_bytes(serialization.Encoding.PEM))

def client_cert():
    with open('cert/ca.pem', 'rb') as ca_file:
        ca_cert = x509.load_pem_x509_certificate(ca_file.read(), default_backend())

    # Load the CSR
    with open('cert/client/csr.pem', 'rb') as csr_file:
        csr = x509.load_pem_x509_csr(csr_file.read(), default_backend())

    with open('cert/key.pem', 'rb') as key_file:
        ca_key = serialization.load_pem_private_key(
            key_file.read(),
            password=b'hello',
            backend=default_backend()
        )

    # Generate the certificate
    cert = (
        x509.CertificateBuilder()
        .subject_name(csr.subject)
        .issuer_name(ca_cert.subject)
        .public_key(csr.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(ca_cert.not_valid_before)
        .not_valid_after(ca_cert.not_valid_after)
        .sign(ca_key, ca_cert.signature_hash_algorithm)
    )

    # Save the certificate to a file
    with open('cert/client/cert.pem', 'wb') as cert_file:
        cert_file.write(cert.public_bytes(serialization.Encoding.PEM))


if __name__ == '__main__':
    generatec_ca()
    server_csr()
    server_cert()
    client_csr()
    client_cert()

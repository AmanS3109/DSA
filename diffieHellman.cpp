#include <iostream>
#include <cmath>

// Function to calculate the modular exponentiation a^b mod p
long long power(long long a, long long b, long long p) {
    long long result = 1;
    a = a % p;

    while (b > 0) {
        if (b & 1)
            result = (result * a) % p;
        b = b >> 1;
        a = (a * a) % p;
    }
    return result;
}

// Function to perform Diffie-Hellman key exchange
long long diffieHellman(long long prime, long long primitiveRoot, long long privateKey) {
    return power(primitiveRoot, privateKey, prime);
}

int main() {
    // Common prime and primitive root
    long long prime = 71;
    long long primitiveRoot = 7;

    // Private keys for users A and B
    long long privateKeyA = 5;
    long long privateKeyB = 12;

    // Calculate public keys for users A and B
    long long publicKeyA = diffieHellman(prime, primitiveRoot, privateKeyA);
    long long publicKeyB = diffieHellman(prime, primitiveRoot, privateKeyB);

    // Display public keys
    std::cout << "Public key for User A: " << publicKeyA << std::endl;
    std::cout << "Public key for User B: " << publicKeyB << std::endl;

    // Calculate shared secret key for both users
    long long sharedSecretA = power(publicKeyB, privateKeyA, prime);
    long long sharedSecretB = power(publicKeyA, privateKeyB, prime);

    // Display shared secret keys
    std::cout << "Shared secret key for User A: " << sharedSecretA << std::endl;
    std::cout << "Shared secret key for User B: " << sharedSecretB << std::endl;

    return 0;
}
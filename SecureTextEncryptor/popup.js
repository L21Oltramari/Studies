document.onload = function() {
  chrome.storage.sync.get('key', function(result) {
    var key;
    if (result.key === undefined) {
      key = forge.random.getBytesSync(32);
      chrome.storage.sync.set({key: key});
    } else {
      key = result.key;
    }

    // Check if event listeners are being added
    console.log("Adding event listeners...");

    document.getElementById('encryptBtn').addEventListener('click', function() {
      console.log("Encrypt button clicked");

      var input = document.getElementById('input').value;
      console.log("Input text:", input);

      var encryptedText;
      try {
        encryptedText = encryptText(input, key);
        console.log("Encrypted text:", encryptedText);
        document.getElementById('output').innerText = encryptedText;
      } catch (error) {
        console.error("Encryption error:", error);
        alert("Encryption failed! Check the console for details.");
      }
    });

    document.getElementById('decryptBtn').addEventListener('click', function() {
      console.log("Decrypt button clicked");

      var encryptedText = document.getElementById('output').innerText;
      try {
        var decryptedText = decryptText(encryptedText, key);
        console.log("Decrypted text:", decryptedText);
        document.getElementById('input').value = decryptedText;
      } catch (error) {
        console.error("Decryption error:", error);
        alert("Decryption failed! Check the console for details.");
      }
    });

    document.getElementById('copyBtn').addEventListener('click', function() {
      console.log("Copy button clicked");
      var outputText = document.getElementById('output').innerText;
      console.log("Text to copy:", outputText);

      // Ensure clipboard permission is declared in manifest.json
      if (!navigator.clipboard) {
        alert("Clipboard functionality not supported by your browser.");
        return;
      }

      navigator.clipboard.writeText(outputText)
        .then(() => {
          console.log("Text copied to clipboard successfully.");
        })
        .catch(err => {
          console.error("Error copying text to clipboard:", err);
          alert("Failed to copy text to clipboard!");
        });
    });
  });
};

function encryptText(text, key) {
  var iv = forge.random.getBytesSync(16); // 128-bit IV
  console.log("Generated IV:", iv);

  var cipher = forge.cipher.createCipher('AES-CFB', key);
  cipher.start({ iv: iv });
  cipher.update(forge.util.createBuffer(text, 'utf8'));
  cipher.finish();

  var encrypted = cipher.output.getBytes();

  var encodedIV = forge.util.encode64(iv);
  var encodedText = forge.util.encode64(encrypted);

  return encodedIV + ':' + encodedText;
}

function decryptText(text, key) {
  var parts = text.split(':');
  var encodedIV = parts[0];
  console.log("Decoded IV:", forge.util.decode64(encodedIV));

  var encodedText = parts[1];
  console.log("Decoded text:", forge.util.decode64(encodedText));

  var decipher = forge.cipher.createDecipher('AES-CFB', key);
  decipher.start({ iv: forge.util.decode64(encodedIV) });
  decipher.update(forge.util.createBuffer(encodedText));
  decipher.finish();

  return decipher.output.toString('utf8');
}

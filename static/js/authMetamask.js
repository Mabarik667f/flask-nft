
function checkMetamaskLogin() {
    fetch('/get-session/')
    .then(response => response.json())
    .then(data => {
        if (!data.address || !window.walletAddress) {
            connectWalletWithMetaMask();
        }
        return data.address
    })
    .catch(error => {
        console.log(error);
    })
}

async function connectWalletWithMetaMask() {
    const address = await window.ethereum.request({method: 'eth_requestAccounts'});
    const response = await fetch(`/set-session/${address}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({'address': address})   
    });

}

document.addEventListener("DOMContentLoaded", function() {
    const address = checkMetamaskLogin();
    window.walletAddress = address;
})

// frontend/app.js
document.getElementById('ruleForm').addEventListener('submit', function(e) {
    e.preventDefault();
    let rule = document.getElementById('rule').value;

    fetch('/create_rule', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ rule_string: rule })
    })
    .then(response => response.json())
    .then(data => {
        console.log('AST:', data);
        // Display AST or process further
    });
});

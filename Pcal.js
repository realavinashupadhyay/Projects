function appendValue(value) {
    document.getElementById("result").value += value;
}

function clearDisplay() {
    document.getElementById("result").value = "";
}

function calculateResult() {
    try {
        let expression = document.getElementById("result").value;
        expression = expression.replace(/√/g, "Math.sqrt");
        let result = eval(expression);
        document.getElementById("result").value = result;
    } catch {
        alert("Invalid Expression");
    }
}

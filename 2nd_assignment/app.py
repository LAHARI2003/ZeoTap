# backend/app.py
from flask import Flask, request, jsonify
from rule_ast import create_rule, combine_rules, evaluate_rule


app = Flask(__name__)

@app.route('/create_rule', methods=['POST'])
def create_rule_api():
    rule_string = request.json.get('rule_string')
    ast = create_rule(rule_string)
    return jsonify({"ast": ast})  # Serialize the AST

@app.route('/combine_rules', methods=['POST'])
def combine_rules_api():
    rules = request.json.get('rules')
    combined_ast = combine_rules(rules)
    return jsonify({"combined_ast": combined_ast})

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_api():
    ast = request.json.get('ast')
    data = request.json.get('data')
    result = evaluate_rule(ast, data)
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)

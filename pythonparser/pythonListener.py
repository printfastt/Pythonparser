# Generated from python.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .pythonParser import pythonParser
else:
    from pythonParser import pythonParser

# This class defines a complete listener for a parse tree produced by pythonParser.
class pythonListener(ParseTreeListener):

    # Enter a parse tree produced by pythonParser#program.
    def enterProgram(self, ctx:pythonParser.ProgramContext):
        pass

    # Exit a parse tree produced by pythonParser#program.
    def exitProgram(self, ctx:pythonParser.ProgramContext):
        pass


    # Enter a parse tree produced by pythonParser#body.
    def enterBody(self, ctx:pythonParser.BodyContext):
        pass

    # Exit a parse tree produced by pythonParser#body.
    def exitBody(self, ctx:pythonParser.BodyContext):
        pass


    # Enter a parse tree produced by pythonParser#block.
    def enterBlock(self, ctx:pythonParser.BlockContext):
        pass

    # Exit a parse tree produced by pythonParser#block.
    def exitBlock(self, ctx:pythonParser.BlockContext):
        pass


    # Enter a parse tree produced by pythonParser#statement.
    def enterStatement(self, ctx:pythonParser.StatementContext):
        pass

    # Exit a parse tree produced by pythonParser#statement.
    def exitStatement(self, ctx:pythonParser.StatementContext):
        pass


    # Enter a parse tree produced by pythonParser#assignment.
    def enterAssignment(self, ctx:pythonParser.AssignmentContext):
        pass

    # Exit a parse tree produced by pythonParser#assignment.
    def exitAssignment(self, ctx:pythonParser.AssignmentContext):
        pass


    # Enter a parse tree produced by pythonParser#expression.
    def enterExpression(self, ctx:pythonParser.ExpressionContext):
        pass

    # Exit a parse tree produced by pythonParser#expression.
    def exitExpression(self, ctx:pythonParser.ExpressionContext):
        pass


    # Enter a parse tree produced by pythonParser#if_statement.
    def enterIf_statement(self, ctx:pythonParser.If_statementContext):
        pass

    # Exit a parse tree produced by pythonParser#if_statement.
    def exitIf_statement(self, ctx:pythonParser.If_statementContext):
        pass


    # Enter a parse tree produced by pythonParser#elif_statement.
    def enterElif_statement(self, ctx:pythonParser.Elif_statementContext):
        pass

    # Exit a parse tree produced by pythonParser#elif_statement.
    def exitElif_statement(self, ctx:pythonParser.Elif_statementContext):
        pass


    # Enter a parse tree produced by pythonParser#else_statement.
    def enterElse_statement(self, ctx:pythonParser.Else_statementContext):
        pass

    # Exit a parse tree produced by pythonParser#else_statement.
    def exitElse_statement(self, ctx:pythonParser.Else_statementContext):
        pass


    # Enter a parse tree produced by pythonParser#while_loop.
    def enterWhile_loop(self, ctx:pythonParser.While_loopContext):
        pass

    # Exit a parse tree produced by pythonParser#while_loop.
    def exitWhile_loop(self, ctx:pythonParser.While_loopContext):
        pass


    # Enter a parse tree produced by pythonParser#for_loop.
    def enterFor_loop(self, ctx:pythonParser.For_loopContext):
        pass

    # Exit a parse tree produced by pythonParser#for_loop.
    def exitFor_loop(self, ctx:pythonParser.For_loopContext):
        pass


    # Enter a parse tree produced by pythonParser#iterable.
    def enterIterable(self, ctx:pythonParser.IterableContext):
        pass

    # Exit a parse tree produced by pythonParser#iterable.
    def exitIterable(self, ctx:pythonParser.IterableContext):
        pass


    # Enter a parse tree produced by pythonParser#condition.
    def enterCondition(self, ctx:pythonParser.ConditionContext):
        pass

    # Exit a parse tree produced by pythonParser#condition.
    def exitCondition(self, ctx:pythonParser.ConditionContext):
        pass


    # Enter a parse tree produced by pythonParser#comparison.
    def enterComparison(self, ctx:pythonParser.ComparisonContext):
        pass

    # Exit a parse tree produced by pythonParser#comparison.
    def exitComparison(self, ctx:pythonParser.ComparisonContext):
        pass


    # Enter a parse tree produced by pythonParser#term.
    def enterTerm(self, ctx:pythonParser.TermContext):
        pass

    # Exit a parse tree produced by pythonParser#term.
    def exitTerm(self, ctx:pythonParser.TermContext):
        pass


    # Enter a parse tree produced by pythonParser#factor.
    def enterFactor(self, ctx:pythonParser.FactorContext):
        pass

    # Exit a parse tree produced by pythonParser#factor.
    def exitFactor(self, ctx:pythonParser.FactorContext):
        pass


    # Enter a parse tree produced by pythonParser#array.
    def enterArray(self, ctx:pythonParser.ArrayContext):
        pass

    # Exit a parse tree produced by pythonParser#array.
    def exitArray(self, ctx:pythonParser.ArrayContext):
        pass



del pythonParser
import java.util.HashMap;

@SuppressWarnings("CheckReturnValue")
public class VInterpreter extends CalculatorBaseVisitor<String> {
   protected static HashMap<String, String> vars = new HashMap<>();
   
   @Override public String visitStatExpr(CalculatorParser.StatExprContext ctx) {
      String res = visit(ctx.expr());
      
      if (res != null){
         String originalAssigmExpr = ctx.getText().strip();
         System.out.println(String.format("%s -> %s", originalAssigmExpr, res));
      }

      return res;
   }

   @Override public String visitStatAssigment(CalculatorParser.StatAssigmentContext ctx) {
      String res = visit(ctx.assigment());
      return res;
   }

   @Override public String visitAssigment(CalculatorParser.AssigmentContext ctx) {
      String res = null;
      String varName = ctx.ID().getText();
      String e = visit(ctx.e);

      if (e != null){
         vars.put(varName, e);
         String originalAssigmExpr = ctx.getText().strip();
         System.out.println(String.format("%s -> %s = %s", originalAssigmExpr, varName, e));
      }

      return res;
   }

   @Override public String visitExprAddSub(CalculatorParser.ExprAddSubContext ctx) {
      String res = null;
      String e1 = visit(ctx.e1);
      String e2 = visit(ctx.e2);
      String op = ctx.op.getText();
      
      if(e1 != null && e2 != null){
         res = String.format("%s %s %s", e1, e2, op);
      }

      return res;
   }

   @Override public String visitExprParent(CalculatorParser.ExprParentContext ctx) {
      String res = visit(ctx.e);
      return res;
   }

   @Override public String visitExprUnary(CalculatorParser.ExprUnaryContext ctx) {
      String res = null;
      String e = visit(ctx.e);
      String op = ctx.op.getText();
      
      if(e != null){
         res = String.format("%s !%s", e, op);
      }

      return res;
   }

   @Override public String visitExprInteger(CalculatorParser.ExprIntegerContext ctx) {
      String res = ctx.INTEGER().getText();
      return res;
   }

   @Override public String visitExprId(CalculatorParser.ExprIdContext ctx) {
      String res = null;
      String varName = ctx.ID().getText();

      if (!vars.containsKey(varName))
         System.err.println("ERROR: Variable <" + varName + "> not defined!");
      else{
         res = vars.get(varName);
      }

      return res;
   }

   @Override public String visitExprMultDivMod(CalculatorParser.ExprMultDivModContext ctx) {
      String res = null;
      String e1 = visit(ctx.e1);
      String e2 = visit(ctx.e2);
      String op = ctx.op.getText();
      
      if(e1 != null && e2 != null){
         res = String.format("%s %s %s", e1, e2, op);
      }

      return res;
   }
}

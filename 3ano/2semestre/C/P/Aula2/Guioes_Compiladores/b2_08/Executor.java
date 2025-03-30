import java.util.HashMap;
import java.util.Map;

@SuppressWarnings("CheckReturnValue")
public class Executor extends CalculatorBaseVisitor<String> {

   protected Map<String,String> variables = new HashMap<>();

   @Override public String visitAssignmentStat(CalculatorParser.AssignmentStatContext ctx) {
      String res = visit(ctx.assignment());
      if(res != null){
         System.out.println(res);
      }
      return res;
   }

   @Override public String visitExprStat(CalculatorParser.ExprStatContext ctx) {
      String res = visit(ctx.expr());
      if(res != null){
         System.out.println(res);
      }
      return res;
   }

   @Override public String visitAssignment(CalculatorParser.AssignmentContext ctx) {
      String number = visit(ctx.expr());
      String ID = ctx.ID().getText();
      variables.put(ID,number);

      return ID + " = " + number;
   }

   @Override public String visitExprAddSub(CalculatorParser.ExprAddSubContext ctx) {
      String res = "";
      String e1 = visit(ctx.expr(0));
      String op = ctx.op.getText();
      String e2 = visit(ctx.expr(1));
      res = e1 + " " + e2 + " " + op;
      return res;
   }

   @Override public String visitExprParent(CalculatorParser.ExprParentContext ctx) {
      return visit(ctx.expr());
   }

   @Override public String visitExperUnary(CalculatorParser.ExperUnaryContext ctx) {
      String res = "";
      String e = visit(ctx.expr());
      String op = ctx.op.getText();
      res = e + " ! " + op;

      return res;
   }

   @Override public String visitExprInteger(CalculatorParser.ExprIntegerContext ctx) {
      return ctx.Integer().getText();
   }

   @Override public String visitExprID(CalculatorParser.ExprIDContext ctx) {
      String id = ctx.ID().getText();

         if(variables.containsKey(id)){
            return variables.get(id);
         }else{
            System.err.println("Variable not found");
            return null;
         }
   }

   @Override public String visitExprMultDivMod(CalculatorParser.ExprMultDivModContext ctx) {
      String res = "";
      String e1 = visit(ctx.expr(0));
      String op = ctx.op.getText();
      String e2 = visit(ctx.expr(1));
      res = e1 + " " + e2 + " "+ op;
      return res;
   }
}

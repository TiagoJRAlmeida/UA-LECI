import java.util.HashMap;
import java.util.Map;

@SuppressWarnings("CheckReturnValue")
   public class Interpreter extends CalculatorBaseVisitor<Integer> {
      
      protected Map<String,Integer> variables = new HashMap<>();

      @Override public Integer visitAssignmentStat(CalculatorParser.AssignmentStatContext ctx) {
         Integer res = visit(ctx.assignment());
            if(res != null){
               System.out.println(res);
            }
            return res;
      }

      @Override public Integer visitExprStat(CalculatorParser.ExprStatContext ctx) {
         Integer res = visit(ctx.expr());
            if(res != null){
               System.out.println(res);
            }
            return res;
      }
      
      @Override public Integer visitAssignment(CalculatorParser.AssignmentContext ctx) {
         Integer number = visit(ctx.expr());
         String ID = ctx.ID().getText();
         variables.put(ID,number);

         return number;
      }
      
      @Override public Integer visitExprID(CalculatorParser.ExprIDContext ctx) {
         String id = ctx.ID().getText();

         if(variables.containsKey(id)){
            return variables.get(id);
         }else{
            System.err.println("Variable not found");
            return null;
         }
      }
      
      @Override public Integer visitExperUnary(CalculatorParser.ExperUnaryContext ctx) {
         Integer res = null;
         Integer e = visit(ctx.expr());
         String op = ctx.op.getText();
      
         switch (op) {
            case "-":
               res = (-1) * e;
               break;
            case "+":
               res = e;
               break;
            
            default:
               break;
         }
         return res;
      }
   
      @Override public Integer visitExprAddSub(CalculatorParser.ExprAddSubContext ctx) {
         Integer res = null;
         Integer e1 = visit(ctx.expr(0));
         Integer e2 = visit(ctx.expr(1));
         String op = ctx.op.getText();
   
         if(e1 != null && e2 != null){
            switch(op){
               case "+":
                  res = e1 + e2;
                  break;
               
               case "-":
                  res = e1 - e2;
                  break;
   
               default:
                  break;
            }
         }
   
         return res;
      }
   
      @Override public Integer visitExprParent(CalculatorParser.ExprParentContext ctx) {
         return visit(ctx.expr());
      }
   
      @Override public Integer visitExprInteger(CalculatorParser.ExprIntegerContext ctx) {
         return Integer.parseInt(ctx.Integer().getText());
      }
   
      @Override public Integer visitExprMultDivMod(CalculatorParser.ExprMultDivModContext ctx) {
         Integer res = null;
         Integer e1 = visit(ctx.expr(0));
         Integer e2 = visit(ctx.expr(1));
         String op = ctx.op.getText();
   
         if(e1 != null && e2 != null){
            switch(op){
               case "*":
                  res = e1 * e2;
                  break;
               
               case "/":
                  res = e1 / e2;
                  break;
               
               case "%":
                  res = e1 % e2;
                  break;
   
               default:
                  break;
            }
         }
   
         return res;
      }
   }
   
   
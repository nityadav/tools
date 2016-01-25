import java.lang.reflect.*;
import java.util.*;

public class DynamicMembersAssignment{

  private static class Template {
    public int count;
    public String name;
    public Template(HashMap<String,String> map) throws NoSuchFieldException, IllegalAccessException
    {
      Field[] members = getClass().getFields();
      for (Field f: members) {
        String fname = f.getName();
        String ftype = f.getType().toString();
        if (ftype.equals("int")) {
          int fval = Integer.parseInt(map.get(fname));
          f.set(this, fval);
        }
        else
          f.set(this, map.get(fname));
      }
    }
  }
  
  public static void main(String []args) throws NoSuchFieldException, IllegalAccessException
  {
   HashMap<String,String> map = new HashMap<String,String>();
   map.put("count","5450");
   map.put("name","Nitin");
   Template obj = new Template(map);
   System.out.println(obj.count);
 }
}
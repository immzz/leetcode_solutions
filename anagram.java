import java.util.*;
public class anagram {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) return false;
        HashMap<Character,Integer> map_a = new HashMap<Character,Integer>();
        for(int i=0;i<s.length();i++){
            if(!map_a.containsKey(s.charAt(i))){
                map_a.put(s.charAt(i),0);
            }
            map_a.put(s.charAt(i),map_a.get(s.charAt(i))+1);
        }
        for(int i=0;i<t.length();i++){
            if(!map_a.containsKey(t.charAt(i))){
                return false;
            }
            map_a.put(t.charAt(i),map_a.get(t.charAt(i))-1);
        }
        for (Map.Entry<Character, Integer> entry : map_a.entrySet())
        {
            if(entry.getValue() != 0){
                return false;
            };
        }
        return true;
    }
	
	public static void main(String [] args){
		anagram a = new anagram();
		System.out.println(a.isAnagram("cat","rat"));
	}
}
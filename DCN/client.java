import java.net.*;
import java.io.*;

public class client {
    public static void main(String[] args) throws Exception {
        Socket s = new Socket("127.0.0.1", 4000);

        System.out.print("Enter the filename : ");
        BufferedReader r1 = new BufferedReader(new InputStreamReader(System.in));
        String fname = keyRead.readLine();

        OutputStream o = s.getOutputStream();
        PrintWriter p = new PrintWriter(o, true);
        p.println(fname);
        
        InputStream i = sock.getInputStream();
        BufferedReader r2 = new BufferedReader(new InputStreamReader(i);

        String str;
        while ((str = r2.readLine()) != null) {
            System.out.println(str);
        }

        p.close();
        r2.close();
        r1.close();
        s.close();
    }
}

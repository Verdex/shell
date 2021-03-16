
use std::io::{Read, Write};
use std::net::{TcpListener, TcpStream};

fn main() -> std::io::Result<()> {

    let listener = TcpListener::bind("127.0.0.1:3145")?;

    loop {
        let (mut sock, addr) = listener.accept()?;

        blarg(&mut sock);
        println!("blarg");
    }

    Ok(())
}

fn blarg(x : &mut TcpStream) -> std::io::Result<()> {
    let mut buffer = vec![];
    println!("first");
    x.read_to_end(&mut buffer)?;
    println!("read");
    x.write(&[0, 1, 2])?;
    println!("write");
    Ok(())
}

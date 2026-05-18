

import prisma from "./lib/prisma.js";

async function main() {
  const user = await prisma.user.create({
    data: {
      email: "krish@test.com",

      password: "123456",
    },
  });

  console.log(user);
}

main();

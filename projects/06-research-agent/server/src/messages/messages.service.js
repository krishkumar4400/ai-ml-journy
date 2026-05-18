import prisma from "../lib/prisma.js";



export async function saveMessage(
  chatId,

  role,

  content,
) {
  return prisma.message.create({
    data: {
      chatId,

      role,

      content,
    },
  });
}

export async function getMessages(chatId) {
  return prisma.message.findMany({
    where: {
      chatId,
    },

    orderBy: {
      createdAt: "asc",
    },
  });
}

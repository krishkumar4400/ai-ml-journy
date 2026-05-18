import prisma
from "../lib/prisma.js";

export async function createChat(
  title,

  userId
) {

  return prisma.chat.create({
    data: {

      title,

      userId,
    },
  });
}

export async function getUserChats(
  userId
) {

  return prisma.chat.findMany({

    where: {
      userId,
    },

    orderBy: {
      createdAt: "desc",
    },
  });
}

export async function getChatById(
  chatId,

  userId
) {

  return prisma.chat.findFirst({

    where: {
      id: chatId,

      userId,
    },

    include: {
      messages: true,
    },
  });
}